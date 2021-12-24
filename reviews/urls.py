from django.urls import include, path
from rest_framework.routers import DefaultRouter

from reviews.views import (CategoriesViewSet, CommentViewSet, GenresViewSet,
                           ReviewViewSet, TitlesViewSet)

router = DefaultRouter()
router.register('genres', GenresViewSet, basename='genres')
router.register('categories', CategoriesViewSet, basename='categories')
router.register('titles', TitlesViewSet, basename='titles')
router.register(
    r'titles/(?P<title_id>[0-9]+)/reviews',
    ReviewViewSet,
    basename='review_by_post',
)
router.register(
    r'titles/(?P<title_id>[0-9]+)/reviews/(?P<review_id>[0-9]+)/comments',
    CommentViewSet,
    basename='comments_by_review',
)

urlpatterns = [
    path('v1/', include(router.urls)),
]
