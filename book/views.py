from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from book.models import Book, Category
from book.serializers import BookSerializer, CategorySerializer
# Create your views here.

class BookViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer