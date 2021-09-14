from api_yamdb.api.filters import CustomFilter
from .models import Category, Genre, Title
from rest_framework import filters, viewsets
from rest_framework.permissions import IsAuthenticated
from django.db.models import Avg

from api_yamdb.reviews.permissions import AdminOrReadOnly
from api_yamdb.reviews.serializers import (
    GenresSerializer, CategoriesSerializer, TitleSerializer,TitleAdminSerializer)


class CategoriesViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategoriesSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = (AdminOrReadOnly,)
    search_fields = ['name',]
    lookup_field = 'slug'


class GenresViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenresSerializer
    permission_classes = (AdminOrReadOnly,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ['name',]
    lookup_field = 'slug'


class TitlesViewSet(viewsets.ModelViewSet):
    queryset = Title.objects.all().annotate(rating=Avg('reviews__score'))
    permission_classes = (AdminOrReadOnly,)
    filterset_class = CustomFilter

    def get_serializer_class(self):
        if self.action in ['create', 'partial_update', 'destroy']:
            return TitleAdminSerializer
        return TitleSerializer
