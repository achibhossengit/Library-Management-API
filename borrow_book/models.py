from django.db import models
from book.models import Book
from django.contrib.auth.models import User
# Create your models here.

class BorrowRecord(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='borrow_record')
    member = models.ForeignKey(User, on_delete=models.CASCADE, related_name='borrow_record')
    borrow_date = models.DateField(auto_now_add=True)
    due_date = models.DateField()
    return_on = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"Record of {self.member.username}"