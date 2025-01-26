from django.db import models


class GenreChoices(models.TextChoices):
    Horror = 'horror','Horror'
    Fantasy = 'fantasy','Fantasy'
    Sci_Fi = 'sci_fi','Sci_Fi'
    Romance = 'romance','Romance'
    Action = 'action','Action'
    Adventure = 'adventure','Adventure'
    Science = 'science','Science'
    Fiction = 'fiction','Fiction'
    Sport = 'sport','Sport'

class Movie(models.Model):
    title = models.CharField(max_length=255)
    director = models.CharField(max_length=255)
    genre = models.CharField(max_length=100, choices=GenreChoices.choices)
    release_date = models.DateField()
    rating = models.CharField(max_length=10)

    def __str__(self):
        return self.title
    

