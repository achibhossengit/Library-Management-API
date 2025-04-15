from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from author.serializers import AuthorSerializer, AuthorBookSerializer
from author.models import Author
from book.models import Book
from book.serializers import BookSerializer
from api.permissions import IsAdminOrLibrarianOrReadOnly
# Create your views here.

class AuthorViewSet(ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = [IsAdminOrLibrarianOrReadOnly]

class AuthorsBookViewSet(ModelViewSet):
    permission_classes = [IsAdminOrLibrarianOrReadOnly]

    def get_serializer_class(self):
        if self.request.method == 'POST' or self.request.method == 'PUT':
            return AuthorBookSerializer
        else:
            return BookSerializer
    def get_queryset(self):
        return Book.objects.filter(author_id=self.kwargs['author_pk'])

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['author_pk'] = self.kwargs['author_pk']
        return context
    
    