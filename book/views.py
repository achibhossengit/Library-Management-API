from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from book.models import Book, Category
from book.serializers import BookSerializer, CategorySerializer
from api.permissions import IsAdminOrLibrarianOrReadOnly
# Create your views here.

class BookViewSet(ModelViewSet):
    """
        API endpoint to manage books.

        - **GET**: List all books or retrieve a single book by ID.
        - **POST**: Create a new book. (*Admin/Librarian only*)
        - **PUT/PATCH**: Update a book by ID. (*Admin/Librarian only*)
        - **DELETE**: Delete a book by ID. (*Admin/Librarian only*)

        **Permissions**: Read-only for all, full access for Admin/Librarian.
    """

    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAdminOrLibrarianOrReadOnly]


class CategoryViewSet(ModelViewSet):
    """
        API endpoint to manage categories.

        - **GET**: List all categories or retrieve a single category by ID.
        - **POST**: Create a new category. (*Admin/Librarian only*)
        - **PUT/PATCH**: Update a category by ID. (*Admin/Librarian only*)
        - **DELETE**: Delete a category by ID. (*Admin/Librarian only*)

        **Permissions**: Read-only for all, full access for Admin/Librarian.
    """

    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAdminOrLibrarianOrReadOnly]
