from django.urls import path
from rest_framework.routers import DefaultRouter

from apps.users.views import UserViewSet, FollowUserAPIView, UnfollowUserAPIView, TokenLogoutAPIView, TokenLoginAPIView
from apps.titles.views import GenresViewSet, PersonViewSet, FilmViewSet, SeriesViewSet, FranchisesViewSet, \
    ReviewViewSet, CountryViewSet

router = DefaultRouter()
router.register(
    'user',
    UserViewSet,
    basename='user',
)
router.register(
    'genres',
    GenresViewSet,
    basename='genres'
)
router.register(
    'person',
    PersonViewSet,
    basename='person'
)
router.register(
    'film',
    FilmViewSet,
    basename='film'
)
router.register(
    'series',
    SeriesViewSet,
    basename='series'
)
router.register(
    'franchises',
    FranchisesViewSet,
    basename='franchises'
)
router.register(
    'review',
    ReviewViewSet,
    basename='review'
)
router.register(
    'country',
    CountryViewSet,
    basename='country'
)

urlpatterns = [
    path('user/follow/', FollowUserAPIView.as_view()),
    path('user/unfollow/', UnfollowUserAPIView.as_view()),
    path('user/token/create/', TokenLoginAPIView.as_view()),
    path('user/token/logout/', TokenLogoutAPIView.as_view())
]
urlpatterns += router.urls
