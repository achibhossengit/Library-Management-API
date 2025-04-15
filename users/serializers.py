from djoser.serializers import UserCreateSerializer
from django.contrib.auth.models import Group

class CustomUserCreateSerializer(UserCreateSerializer):
    def create(self, validated_data):
        user = super().create(validated_data)
        group, create = Group.objects.get_or_create(name='Member')
        # user.groups.add(group[0].id)
        user.groups.add(group)

        return user