from django.db import models

import re

# Create your models here.

class UserManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if len(postData['firstNameLabel']) < 2 :
            errors['firstNameLabel'] = "First Name should not be less than 2 characters"
        if len(postData['lastNameLabel']) < 2:
            errors['lastNameLabel'] = "Last Name should not be less than 2 characters"
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(postData['emailLabel']): 
            errors['emailLabel'] = "Invalid email address!"
        if len(postData['passwordLabel']) < 8:
            errors['passwordLabel'] = "Please enter at least 8 characters for your password"
        if postData['passwordLabel'] != postData['passwordConfirmLabel']:
            errors['pw_confirm'] = "please ensure that your password matches the confirmation"
        return errors


class User(models.Model):
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    email = models.EmailField()
    password = models.CharField(max_length=64)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()


class JobManager(models.Manager):
    def basic_validator_two(self, postData):
        errors = {}

        if len(postData['titleLabel']) < 3:
            errors['titleLabel'] = "Title characters should not be less than 3 characters"
        if len(postData['descriptionLabel']) < 3:
            errors['descriptionLabel'] = "Description characters should not be less than 3 characters"
        if len(postData['locationLabel']) < 3:
            errors['locationLabel'] = "Location characters should not be less than 3 characters"
        return errors
        




class Job(models.Model):
    title = models.CharField(max_length=64)
    description = models.TextField()
    location = models.CharField(max_length=64)
    user_created = models.ForeignKey(User, related_name='jobsCreated', on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = JobManager()