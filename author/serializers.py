from rest_framework.serializers import ModelSerializer
from author.models import Author
from book.models import Book
class AuthorSerializer(ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'

class AuthorBookSerializer(ModelSerializer):
    class Meta:
        model = Book
        fields = ['title', 'copies', 'category']
        
    def create(self, validated_data):
        return Book.objects.create(author_id=self.context['author_pk'], **validated_data)

    def update(self, instance, validated_data):
        instance.author_id = self.context['author_pk']
        instance.title = validated_data.get('title', instance.title)
        instance.copies = validated_data.get('copies', instance.copies)
        instance.category = validated_data.get('category', instance.category)
        instance.save()
        return instance
