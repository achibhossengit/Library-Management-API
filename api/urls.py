from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_nested.routers import NestedDefaultRouter
from book.views import BookViewSet, CategoryViewSet
from author.views import AuthorViewSet, AuthorsBookViewSet
from borrow_book.views import BorrowViewSet

routers = DefaultRouter()
routers.register('books', BookViewSet)
routers.register('categories', CategoryViewSet)
routers.register('authors', AuthorViewSet)
routers.register('borrow-list', BorrowViewSet)

author_router = NestedDefaultRouter(routers,'authors', lookup='author')
author_router.register('books', AuthorsBookViewSet, basename='author-books')

urlpatterns = [
    path('', include(routers.urls)),
    path('', include(author_router.urls)),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
]

