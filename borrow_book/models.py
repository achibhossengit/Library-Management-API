from django.db import models
from book.models import Book
from users.models import Member
# Create your models here.

class BorrowRecord(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='borrow_record')
    member = models.ForeignKey(Member, on_delete=models.CASCADE, related_name='borrow_record')
    borrow_date = models.DateField(auto_now_add=True)
    due_date = models.DateField()
    return_on = models.DateField(null=True, blank=True)