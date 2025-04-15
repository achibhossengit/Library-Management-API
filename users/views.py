from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from django.contrib.auth.models import User, Group
from djoser.serializers import UserSerializer
from api.permissions import IsAdminOrLibrarian
from rest_framework.permissions import SAFE_METHODS

class MemberViewSet(ModelViewSet):
    http_method_names = ['get', 'head', 'option']
    group = Group.objects.get(name='Member')
    queryset = User.objects.filter(groups=group)
    serializer_class = UserSerializer
    permission_classes = [IsAdminOrLibrarian]