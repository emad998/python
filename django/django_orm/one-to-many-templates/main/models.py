from django.db import models

# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    email = models.EmailField(max_length=64)
    fav_number = models.IntegerField()
    motto = models.TextField()
    # is_active = models.BooleanField(default=True)

    # albums - this is being created by the "related_name" below

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

# creating our Album model
# inheriting from the Model class
class Album(models.Model):
    # creating an instance of the CharField class
    # assigning it to the class attribute "artist"
    artist = models.CharField(max_length=64)
    title = models.CharField(max_length=64)
    release_date = models.DateField(default="2020-06-09")
    genre = models.CharField(max_length=20)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    owner = models.ForeignKey(
        # owner will be an instance of the User class
        User,
        # if owner gets deleted, all of his/her albums get deleted too
        on_delete=models.CASCADE,
        # creates a "hidden field" in the User class
        # that references all that user's albums
        related_name="albums"
    )