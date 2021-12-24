from django.urls import include, path
from rest_framework.routers import DefaultRouter

from users.views import UserViewSet, get_jwt_token, signup


router = DefaultRouter()
router.register('users', UserViewSet, basename='users')

URLS = [
    path('auth/signup/', signup, name='signup'),
    path('auth/token/', get_jwt_token, name='token'),
]

URLS += router.urls

urlpatterns = [
    path('v1/', include(URLS)),
]
