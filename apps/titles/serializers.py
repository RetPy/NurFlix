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
    total_score = serializers.SerializerMethodField()

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
            'total_score'
        )

    def get_total_score(self, obj):
        reviews = obj.review_title.all()
        try:
            total_score = sum(i.score for i in reviews) / len(reviews)
        except ZeroDivisionError:
            total_score = 0
        return total_score


class SeriesSerializer(serializers.ModelSerializer):
    type = serializers.CharField(read_only=True)
    total_score = serializers.SerializerMethodField()

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
            'total_score'
        )

    def get_total_score(self, obj):
        reviews = obj.review_title.all()
        try:
            total_score = sum(i.score for i in reviews) / len(reviews)
        except ZeroDivisionError:
            total_score = 0
        return total_score


class FranchisesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Franchises
        fields = '__all__'


class ReviewSerializer(serializers.ModelSerializer):
    user = serializers.CharField(read_only=True)

    class Meta:
        model = Reviews
        fields = '__all__'
