from rest_framework.serializers import ModelSerializer
from borrow_book.models import BorrowRecord

class BorrowSerializer(ModelSerializer):
    class Meta:
        model = BorrowRecord
        fields = '__all__'

class RetrunSerializer(ModelSerializer):
    class Meta:
        model = BorrowRecord
        fields = ['return_on',]