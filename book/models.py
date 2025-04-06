from django.db import models
from author.models import Author

# Create your models here.

class Category(models.Model):
    name = models.CharField()
    description = models.TextField()

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='books')
    copies = models.PositiveIntegerField()

    def __str__(self):
        return self.title
