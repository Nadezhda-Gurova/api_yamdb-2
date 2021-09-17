from rest_framework.validators import UniqueValidator
from rest_framework import serializers

from users.models import MyUser


class UserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=MyUser.objects.all())]
    )

    class Meta:
        model = MyUser
        fields = ['email', 'username']

    def validate_username(self, value):
        if 'me' not in value:
            return value
        raise serializers.ValidationError(
            'You cannot use me as your username!')


class UpdateUserSerialier(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=MyUser.objects.all())]
    )

    class Meta:
        model = MyUser
        exclude = [
            'id',
            'password',
            'last_login',
            'is_superuser',
            'is_staff',
            'is_active',
            'date_joined'
        ]


class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyUser
        fields = [
            'username',
            'email',
            'first_name',
            'last_name',
            'bio',
            'role'
        ]
