from django.urls import path, include
from book.views import BookViewSet, CategoryViewSet
from author.views import AuthorViewSet, AuthorsBookViewSet
from rest_framework.routers import DefaultRouter
from rest_framework_nested.routers import NestedDefaultRouter

routers = DefaultRouter()
routers.register('books', BookViewSet)
routers.register('categories', CategoryViewSet)
routers.register('authors', AuthorViewSet)

author_router = NestedDefaultRouter(routers,'authors', lookup='author')
author_router.register('books', AuthorsBookViewSet, basename='author-books')

urlpatterns = [
    path('', include(routers.urls)),
    path('', include(author_router.urls)),
    # path('authors/<author_pk>/books', AuthorsBookViewSet.as_view({'get':'list'})),
    # path('authors/<author_pk>/books/<pk>/', AuthorsBookViewSet.as_view({'get':'retrieve'})),
]

