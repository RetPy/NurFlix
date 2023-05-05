from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Genres(models.Model):
    name = models.CharField(
        max_length=255,
    )
    description = models.TextField()
    picture = models.ImageField(
        upload_to='genres/',
    )

    def __str__(self):
        return self.name


class Country(models.Model):
    name = models.CharField(
        max_length=255,
    )

    def __str__(self):
        return self.name


class Person(models.Model):
    first_name = models.CharField(
        max_length=255,
    )
    last_name = models.CharField(
        max_length=255,
    )
    avatar = models.ImageField(
        upload_to='person_image',
        null=True,
        blank=True,
    )
    bio = models.TextField()
    age = models.PositiveIntegerField(
        default=1,
    )
    birthdate = models.DateField()
    birth_place = models.CharField(
        max_length=500,
    )
    death_date = models.DateField(
        null=True,
        blank=True,
    )
    height = models.PositiveIntegerField(
        default=100,
    )
    partner = models.ForeignKey(
        'self',
        on_delete=models.SET_NULL,
        related_name='person_partner',
        null=True,
        blank=True,
    )

    def __str__(self):
        return self.first_name


class Title(models.Model):
    TYPE_CHOICE = (
        ('Film', 'Film'),
        ('Series', 'Series'),
    )
    type = models.CharField(
        max_length=10,
        choices=TYPE_CHOICE,
    )
    name = models.CharField(
        max_length=500,
    )
    description = models.TextField()
    genres = models.ManyToManyField(
        Genres,
        related_name='title_genres',
    )
    actors = models.ManyToManyField(
        Person,
        related_name='title_actors',
    )
    director = models.ManyToManyField(
        Person,
        related_name='title_director',
    )
    v_poster = models.ImageField(
        upload_to='title/v_poster/',
        null=True,
        blank=True,
    )
    h_poster = models.ImageField(
        upload_to='title/h_poster/',
        null=True,
        blank=True,
    )
    release_date = models.DateField()
    trailer_url = models.URLField()
    country = models.ManyToManyField(
        Country,
        related_name='title_country',
    )
    budget = models.IntegerField()
    age_limit = models.CharField(
        max_length=15
    )
    # -film
    film_time = models.PositiveIntegerField(
        null=True,
        blank=True,
    )
    # -series
    episodes = models.PositiveIntegerField(
        null=True,
        blank=True,
    )
    seasons = models.PositiveIntegerField(
        null=True,
        blank=True,
    )
    series_time = models.PositiveIntegerField(
        null=True,
        blank=True,
    )

    def __str__(self):
        return self.name


class Franchises(models.Model):
    name = models.CharField(
        max_length=255,
    )
    description = models.TextField()
    picture = models.ImageField(
        upload_to='franchises/',
    )
    title = models.ForeignKey(
        Title,
        on_delete=models.CASCADE,
        related_name='franchises_title',
    )

    def __str__(self):
        return self.name


class Reviews(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='review_user',
    )
    title = models.ForeignKey(
        Title,
        on_delete=models.CASCADE,
        related_name='review_title',
    )
    text = models.TextField()
    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    def __str__(self):
        return f'{self.user}: {self.title}'
