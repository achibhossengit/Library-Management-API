from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from author.serializers import AuthorSerializer, AuthorBookSerializer
from author.models import Author
from book.models import Book
from book.serializers import BookSerializer
from api.permissions import IsAdminOrLibrarianOrReadOnly
# Create your views here.

class AuthorViewSet(ModelViewSet):
    """
        API endpoint to manage authors.

        - **GET**: List all authors or retrieve a single author by ID.
        - **POST**: Create a new author. (*Admin/Librarian only*)
        - **PUT**: Update an author by ID. (*Admin/Librarian only*)
        - **DELETE**: Delete an author by ID. (*Admin/Librarian only*)

        **Permissions**: Read-only for all, full access for Admin/Librarian.
    """

    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = [IsAdminOrLibrarianOrReadOnly]

class AuthorsBookViewSet(ModelViewSet):
    """
        API endpoint to manage books for a specific author.

        - **GET**: List all books for the specified author.
        - **POST**: Add a new book for the specified author. (*Admin/Librarian only*)
        - **PUT**: Update a book for the specified author. (*Admin/Librarian only*)
        - **DELETE**: Delete a book for the specified author. (*Admin/Librarian only*)

        **Serializer**:
        - **POST/PUT**: Uses `AuthorBookSerializer`.
        - **Other Methods**: Uses `BookSerializer`.

        **Permissions**: Read-only for all, full access for Admin/Librarian.
    """

    permission_classes = [IsAdminOrLibrarianOrReadOnly]

    def get_serializer_class(self):
        if self.request.method == 'POST' or self.request.method == 'PUT':
            return AuthorBookSerializer
        else:
            return BookSerializer
    def get_queryset(self):
        return Book.objects.filter(author_id=self.kwargs.get('author_pk'))

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['author_pk'] = self.kwargs.get('author_pk')
        return context
    