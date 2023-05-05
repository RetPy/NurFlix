from rest_framework import serializers

from apps.titles.models import Genres, Person, Title, Franchises, Reviews, Country


class GenresSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genres
        fields = '__all__'


class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = '__all__'


class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = '__all__'


class FilmSerializer(serializers.ModelSerializer):
    type = serializers.CharField(read_only=True)

    class Meta:
        model = Title
        fields = (
            'id',
            'name',
            'type',
            'description',
            'genres',
            'actors',
            'director',
            'v_poster',
            'h_poster',
            'release_date',
            'trailer_url',
            'country',
            'budget',
            'age_limit',
            'film_time',
            'type',
        )


class SeriesSerializer(serializers.ModelSerializer):
    type = serializers.CharField(read_only=True)

    class Meta:
        model = Title
        fields = (
            'id',
            'name',
            'type',
            'description',
            'genres',
            'actors',
            'director',
            'v_poster',
            'h_poster',
            'release_date',
            'trailer_url',
            'country',
            'budget',
            'age_limit',
            'episodes',
            'seasons',
            'series_time',
        )


class FranchisesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Franchises
        fields = '__all__'


class ReviewSerializer(serializers.ModelSerializer):
    user = serializers.CharField(read_only=True)

    class Meta:
        model = Reviews
        fields = '__all__'
