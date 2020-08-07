from django.db import models
import re
from django.contrib import messages
import bcrypt


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
            errors["password"] = "Password is too short"
        return errors


class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    password = models.CharField(max_length=255)
    confirm_pw = models.CharField(max_length=255)
    objects = User_manager()


class Plant(models.Model):
    plant_type = models.CharField(max_length=64)
    light = models.CharField(max_length=64)
    description = models.TextField()
    user = models.ForeignKey(
        User, related_name="plants", on_delete=models.CASCADE)
    img = models.TextField(default="hi")


    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Comment(models.Model):
    comment = models.TextField()
    user = models.ForeignKey(
        User, related_name="comments", on_delete=models.CASCADE)
    plant = models.ForeignKey(
        Plant, related_name="comments", on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
