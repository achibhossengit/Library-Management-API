from rest_framework.permissions import BasePermission, SAFE_METHODS

class IsAdminOrLibrarianOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS: # get, head, option
            return True
            
        if not request.user.is_authenticated:
            return False
            
        if request.user.is_staff:
            return True
            
        return request.user.groups.filter(name='Librarian').exists()
        
        
class IsAdminOrLibrarian(BasePermission):
    def has_permission(self, request, view):
        
        if not request.user.is_authenticated:
            return False
            
        if request.user.is_staff:
            return True
            
        return request.user.groups.filter(name='Librarian').exists()