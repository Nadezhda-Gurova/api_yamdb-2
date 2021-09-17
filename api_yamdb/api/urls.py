from django.urls import include, path
from rest_framework.routers import DefaultRouter

from reviews.views import CategoriesViewSet, GenresViewSet, TitlesViewSet
from users.views import register_user, update_user_info, UserList, UserDetail


router_ver1 = DefaultRouter()

router_ver1.register(r'categories', CategoriesViewSet, basename='categories')
router_ver1.register(r'genres', GenresViewSet, basename='genres')
router_ver1.register(r'titles', TitlesViewSet, basename='titles')

urlpatterns = [
    path('v1/', include(router_ver1.urls)),
    path('v1/auth/signup/', register_user),
    path('v1/users/me/', update_user_info),
    path('v1/users/<str:username>/', UserDetail.as_view()),
    path('v1/users/', UserList.as_view()),
]
