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


class Food(models.Model):
    food_name = models.CharField(max_length=64)
  #  user = models.CharField(max_length=64)
    calories = models.IntegerField()
    fat = models.IntegerField()
    carbs = models.IntegerField()
    fiber = models.IntegerField()
    protein = models.IntegerField()
    image = models.TextField()
    price = models.IntegerField(default=10)

    user_favorite = models.ForeignKey(
        User,
        related_name="user_favorites",
        on_delete = models.CASCADE
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Order(models.Model):
    quantity = models.IntegerField()
    price = models.IntegerField()
    total_calorie = models.IntegerField()

    user = models.ForeignKey(
        User,
        related_name="orders",
        on_delete = models.CASCADE
    )

    food = models.ForeignKey(
        Food,
        related_name="ordered_foods",
        on_delete = models.CASCADE
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)