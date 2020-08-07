from django.db import models
from datetime import date
from datetime import datetime

# Create your models here.

class ShowManager(models.Manager):
    def basic_validator(self, postData):
        errors={}
        if len(postData['titleLabel']) < 3:
            errors['titleLabel'] = "Show title should be at least 3 characters"
        if len(postData['networkLabel']) < 3:
            errors['networkLabel'] = "Show network shoud be at least 3 characters"
        if len(postData['descriptionLabel']) < 2:
            errors['descriptionLabel'] = "Show Description should be at least 2 characters"
        today = date.today()
        if datetime.strptime(postData['releaseDateLabel'], "%Y-%m-%d").date() > today:
            errors['releaseDateLabel'] = "release Date can't be in the future!!!"

        return errors


class Show(models.Model):
    title = models.CharField(max_length=64)
    network = models.CharField(max_length=64)
    release_date = models.DateField()
    description = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = ShowManager()