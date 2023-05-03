from rest_framework import viewsets, permissions

from apps.titles.models import Genres, Person, Title, Franchises, Reviews, Country
from apps.titles.serializers import GenresSerializer, PersonSerializer, FilmSerializer, SeriesSerializer, \
    FranchisesSerializer, ReviewSerializer, CountrySerializer
from utils.permissions import IsOwnerUser


class GenresViewSet(viewsets.ModelViewSet):
    queryset = Genres.objects.all()
    serializer_class = GenresSerializer
    search_fields = ('name',)
    permission_classes_by_action = {
        'list': [permissions.IsAuthenticated],
        'create': [permissions.IsAdminUser],
        'retrieve': [permissions.IsAuthenticated],
        'update': [permissions.IsAdminUser],
        'delete': [permissions.IsAdminUser],
    }

    def get_permissions(self):
        try:
            return [permission() for permission in self.permission_classes_by_action[self.action]]
        except KeyError:
            return [permission() for permission in self.permission_classes]


class CountryViewSet(viewsets.ModelViewSet):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer
    search_fields = ('name',)
    permission_classes_by_action = {
        'list': [permissions.IsAuthenticated],
        'create': [permissions.IsAdminUser],
        'retrieve': [permissions.IsAuthenticated],
        'update': [permissions.IsAdminUser],
        'delete': [permissions.IsAdminUser],
    }

    def get_permissions(self):
        try:
            return [permission() for permission in self.permission_classes_by_action[self.action]]
        except KeyError:
            return [permission() for permission in self.permission_classes]


class PersonViewSet(viewsets.ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
    search_fields = ('name',)
    permission_classes_by_action = {
        'list': [permissions.IsAuthenticated],
        'create': [permissions.IsAdminUser],
        'retrieve': [permissions.IsAuthenticated],
        'update': [permissions.IsAdminUser],
        'delete': [permissions.IsAdminUser],
    }

    def get_permissions(self):
        try:
            return [permission() for permission in self.permission_classes_by_action[self.action]]
        except KeyError:
            return [permission() for permission in self.permission_classes]


class FilmViewSet(viewsets.ModelViewSet):
    queryset = Title.objects.filter(type='Film')
    serializer_class = FilmSerializer
    filterset_fields = ('genres', 'age_limit', 'release_date')
    search_fields = ('name',)
    permission_classes_by_action = {
        'list': [permissions.IsAuthenticated],
        'create': [permissions.IsAdminUser],
        'retrieve': [permissions.IsAuthenticated],
        'update': [permissions.IsAdminUser],
        'delete': [permissions.IsAdminUser],
    }

    def get_permissions(self):
        try:
            return [permission() for permission in self.permission_classes_by_action[self.action]]
        except KeyError:
            return [permission() for permission in self.permission_classes]

    def perform_create(self, serializer):
        serializer.save(type='Film')


class SeriesViewSet(viewsets.ModelViewSet):
    queryset = Title.objects.filter(type='Series')
    serializer_class = SeriesSerializer
    filterset_fields = ('genres', 'age_limit', 'release_date')
    search_fields = ('name',)
    permission_classes_by_action = {
        'list': [permissions.IsAuthenticated],
        'create': [permissions.IsAdminUser],
        'retrieve': [permissions.IsAuthenticated],
        'update': [permissions.IsAdminUser],
        'delete': [permissions.IsAdminUser],
    }

    def get_permissions(self):
        try:
            return [permission() for permission in self.permission_classes_by_action[self.action]]
        except KeyError:
            return [permission() for permission in self.permission_classes]

    def perform_create(self, serializer):
        serializer.save(type='Series')


class FranchisesViewSet(viewsets.ModelViewSet):
    queryset = Franchises.objects.all()
    serializer_class = FranchisesSerializer
    search_fields = ('name',)
    permission_classes_by_action = {
        'list': [permissions.IsAuthenticated],
        'create': [permissions.IsAdminUser],
        'retrieve': [permissions.IsAuthenticated],
        'update': [permissions.IsAdminUser],
        'delete': [permissions.IsAdminUser],
    }

    def get_permissions(self):
        try:
            return [permission() for permission in self.permission_classes_by_action[self.action]]
        except KeyError:
            return [permission() for permission in self.permission_classes]


class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Reviews.objects.all()
    serializer_class = ReviewSerializer
    search_fields = ('name',)
    permission_classes_by_action = {
        'list': [permissions.IsAuthenticated],
        'create': [permissions.IsAuthenticated],
        'retrieve': [permissions.IsAuthenticated],
        'update': [IsOwnerUser | permissions.IsAdminUser],
        'delete': [IsOwnerUser | permissions.IsAdminUser],
    }

    def get_permissions(self):
        try:
            return [permission() for permission in self.permission_classes_by_action[self.action]]
        except KeyError:
            return [permission() for permission in self.permission_classes]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
