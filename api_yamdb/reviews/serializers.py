from django.contrib.auth import password_validation
from django.contrib.auth.hashers import make_password
from django.core import exceptions
from rest_framework import serializers

from .models import Category, Comment, Genre, Review, Title


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        exclude = ['id']
        model = Genre


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        exclude = ['id']
        model = Category


class TitleSerializerCreate(serializers.ModelSerializer):
    genre = serializers.SlugRelatedField(
        slug_field='slug',
        queryset=Genre.objects.all(),
        many=True,
        required=False,
    )
    category = serializers.SlugRelatedField(
        slug_field='slug',
        queryset=Category.objects.all(),
        required=False,
    )

    class Meta:
        fields = '__all__'
        model = Title
        extra_kwargs = {
            'description': {'required': False},
        }


class TitleSerializer(serializers.ModelSerializer):
    genre = GenreSerializer(many=True, read_only=True)
    category = CategorySerializer(read_only=True)
    rating = serializers.FloatField(read_only=True)

    class Meta:
        fields = '__all__'
        model = Title


class ReviewSerializer(serializers.ModelSerializer):
    title = serializers.SlugRelatedField(
        default=None,
        slug_field='id',
        write_only=True,
        queryset=Title.objects.all(),
    )

    author = serializers.SlugRelatedField(
        default=serializers.CurrentUserDefault(),
        read_only=True,
        slug_field='username',
    )

    def validate(self, value):
        title = self.context['request'].parser_context['kwargs']['title_id']
        request = self.context.get('request')
        if (
            request.method == 'POST' \
            and Review.objects.filter(
                title=title, author=request.user
            ).exists()
        ):
            raise serializers.ValidationError(
                'This author has already written a review'
            )
        return value

    class Meta:
        model = Review
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        read_only=True,
        slug_field='username',
    )

    class Meta:
        model = Comment
        exclude = ['review']
        extra_kwargs = {
            'title': {'required': False},
            'review': {'required': False},
        }
