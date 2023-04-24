from django.contrib import admin

from apps.titles.models import Genres, Person, Title, Franchises, Reviews


@admin.register(Genres)
class GenresAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('id', 'name')


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name')
    list_display_links = ('id', 'first_name')
    list_filter = ('id', 'birthdate', 'death_date')
    search_fields = ('id', 'first_name', 'last_name')


@admin.register(Title)
class TitleAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    list_filter = ('id', 'genres', 'type', 'actors', 'director', 'release_date', 'country', 'budget', 'age_limit')
    search_fields = ('id', 'name')


@admin.register(Franchises)
class FranchisesAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('id', 'name')


@admin.register(Reviews)
class ReviewsAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'title', 'created_at')
    list_display_links = ('id', 'user')
    list_filter = ('id', 'user', 'title', 'created_at')
    search_fields = ('id', 'user', 'title')
