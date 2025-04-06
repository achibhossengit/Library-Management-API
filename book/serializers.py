from rest_framework.serializers import ModelSerializer
from book.models import Book, Category


class BookSerializer(ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
        