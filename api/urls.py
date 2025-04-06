from django.urls import path, include
from book.views import BookViewSet, CategoryViewSet
from rest_framework.routers import DefaultRouter

routers = DefaultRouter()
routers.register('books', BookViewSet)
routers.register('categories', CategoryViewSet)

urlpatterns = [
    path('', include(routers.urls))
]

