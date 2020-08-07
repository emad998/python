from django.db import models
from django.db import models
import re
from django.contrib import messages
import bcrypt


class Appointment_manager(models.Manager):
    def appointment_validator(self, postData):
        errors = {}
        if len(postData['task']) < 2:
            errors["task"] = "destination name needs to be at least 2 characters"
        if len(postData['date']) < 2:
            errors["date"] = "date must be mm/dd/year"
        if len(postData['status']) < 1:
            errors["status"] = "status must be filled "
        return errors


class User_manager(models.Manager):
    def registration_validator(self, postData):
        errors = {}
        if len(postData['first_name_input']) < 2:
            errors["first_name"] = "First name needs to be at least 2 characters"
        if len(postData['last_name_input']) < 2:
            errors["last_name"] = "Last name needs to be atleast 2 characters"
        EMAIL_REGEX = re.compile(
            r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(postData['email_input']):
            errors['email'] = "Invalid email address"
        if len(postData['password_input']) < 8:
            errors["password"] = "Password is to short"
        if len(postData['confirm_pw_input']) < 8:
            errors["confirm_password"] = "Confirm PW To Short"
        if postData['password_input'] != postData['confirm_pw_input']:
            errors["password"] = "Passwords do not match"
        return errors

    def login_validator(self, postData):
        errors = {}

        if len(postData['password_input']) < 8:
            errors["password"] = "Password is to short"
        return errors


class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    password = models.CharField(max_length=255)
    confirm_pw = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = User_manager()


class Appointment(models.Model):
    tasks = models.CharField(max_length=64)
    date = models.CharField(max_length=64)
    status = models.CharField(max_length=64)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, related_name='appointments',
                             on_delete=models.CASCADE)
    objects = Appointment_manager()
