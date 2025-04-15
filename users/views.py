from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from django.contrib.auth.models import User, Group
from djoser.serializers import UserSerializer
from api.permissions import IsAdminOrLibrarian
from rest_framework.permissions import SAFE_METHODS

class MemberViewSet(ModelViewSet):
    """
    API endpoint for viewing library members.

    - **GET**: Retrieve a list of members or a specific member by ID.
    - **HEAD/OPTIONS**: Supported for API metadata.
    **Permissions**: Accessible only by Admins or Librarians.
    """

    http_method_names = ['get', 'head', 'option']
    group, create = Group.objects.get_or_create(name='Member')
    queryset = User.objects.filter(groups=group)
    serializer_class = UserSerializer
    permission_classes = [IsAdminOrLibrarian]