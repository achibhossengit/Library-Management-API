from django.db import models

# Create your models here.
class Author(models.Model):
    name = models.CharField()
    bio = models.TextField()

    def __str__(self):
        return self.name