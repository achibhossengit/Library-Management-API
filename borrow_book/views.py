from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from borrow_book.models import BorrowRecord
from borrow_book.serializers import BorrowSerializer, RetrunSerializer
from rest_framework.permissions import IsAuthenticated
from borrow_book.permisssions import IsOwner
from api.permissions import IsAdminOrLibrarianOrReadOnly

# Create your views here.

class BorrowViewSet(ModelViewSet):
    """
        API endpoint for managing borrowing records.

        - **GET**: Staff/Librarians can view all records; members can view their own.
        - **POST**: Create a new borrowing record.
        - **PUT/PATCH**: Update a record (*Owner only*; uses `ReturnSerializer` for PUT).
        - **DELETE**: Delete a record (*Admin/Librarian only*).
    """

    def get_queryset(self):
        if self.request.user.is_staff or self.request.user.groups.filter(name='Librarian').exists():
            return BorrowRecord.objects.all()
        return BorrowRecord.objects.filter(member=self.request.user)
    
    def get_permissions(self):
        if self.action in ['update', 'partial_update']:
            return [IsOwner()]
        if self.action == 'destroy':
            return [IsAdminOrLibrarianOrReadOnly()]
        return [IsAuthenticated()]

    def get_serializer_class(self):
        if self.request.method == 'PUT':
            return RetrunSerializer
        else:
            return BorrowSerializer
        
    def get_serializer_context(self):
        return {'member': self.request.user}