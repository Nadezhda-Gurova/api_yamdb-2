from django.urls import include, path
from rest_framework.routers import DefaultRouter

from api_yamdb.reviews.views import CategoriesViewSet, GenresViewSet, TitlesViewSet

router_ver1 = DefaultRouter()

router_ver1.register(r'categories', CategoriesViewSet, basename='categories')
router_ver1.register(r'genres', GenresViewSet, basename='genres')
router_ver1.register(r'titles', TitlesViewSet, basename='titles')

urlpatterns = [
    path('v1/', include(router_ver1.urls)),
]
