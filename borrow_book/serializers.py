from rest_framework.serializers import ModelSerializer
from borrow_book.models import BorrowRecord

class BorrowSerializer(ModelSerializer):
    class Meta:
        model = BorrowRecord
        fields = ['id','book', 'member', 'borrow_date', 'due_date', 'return_on']
        read_only_fields = ['member', 'borrow_date', 'return_on']

    def create(self, validated_data):
        member = self.context.get('member')
        record = BorrowRecord.objects.create(member=member, **validated_data)
        record.save()
        return record


        

class RetrunSerializer(ModelSerializer):
    class Meta:
        model = BorrowRecord
        fields = ['return_on',]