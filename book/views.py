from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from book.models import Book, Category
from book.serializers import BookSerializer, CategorySerializer
from api.permissions import IsAdminOrLibrarianOrReadOnly
# Create your views here.

class BookViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAdminOrLibrarianOrReadOnly]


class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAdminOrLibrarianOrReadOnly]
