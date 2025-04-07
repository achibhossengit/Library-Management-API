from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from borrow_book.models import BorrowRecord
from borrow_book.serializers import BorrowSerializer, RetrunSerializer

# Create your views here.

class BorrowViewSet(ModelViewSet):
    queryset = BorrowRecord.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'PUT':
            return RetrunSerializer
        else:
            return BorrowSerializer
        
class MemberBorrowViewSet(ModelViewSet):
    http_method_names = ['get', 'post', 'put']
    def get_queryset(self):
        member_id = self.kwargs.get('member_pk')
        queryset = BorrowRecord.objects.filter(member_id = member_id)
        return queryset


    def get_serializer_class(self):
        if self.request.method == 'PUT':
            return RetrunSerializer
        else:
            return BorrowSerializer