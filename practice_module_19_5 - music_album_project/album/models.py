from django.db import models
from musician.models import Musician

# Create your models here.
class Album(models.Model):
    album_name = models.CharField(max_length=20)

    # one to many relationship
    musician = models.ForeignKey(Musician, on_delete=models.CASCADE)

    album_release_date = models.DateField()

    # rating options for choices
    rating_choices = [('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')]
    rating = models.CharField(choices=rating_choices, max_length=1)


    def __str__(self):
        return self.album_name


