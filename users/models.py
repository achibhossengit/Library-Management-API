from django.db import models

# Create your models here.
class Member(models.Model):
    name = models.CharField()
    member_since = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name