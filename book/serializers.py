from rest_framework.serializers import ModelSerializer
from book.models import Book, Category


class BookSerializer(ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

    def save(self, **kwargs):
        return super().save(**kwargs)

class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
        