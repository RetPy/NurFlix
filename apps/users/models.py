from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    bio = models.TextField(
        max_length=100,
        null=True,
        blank=True,
    )
    avatar = models.ImageField(
        upload_to='user_avatar/',
        null=True,
        blank=True,
        default='default_avatar.png'
    )
    liked_actor = models.ForeignKey(
        'titles.Person',
        on_delete=models.SET_NULL,
        related_name='user_liked_actor',
        null=True,
        blank=True,
    )
    liked_director = models.ForeignKey(
        'titles.Person',
        on_delete=models.SET_NULL,
        related_name='user_liked_director',
        null=True,
        blank=True,
    )
    liked_film = models.ForeignKey(
        'titles.Title',
        on_delete=models.SET_NULL,
        related_name='user_liked_film',
        null=True,
        blank=True,
    )
    liked_series = models.ForeignKey(
        'titles.Title',
        on_delete=models.SET_NULL,
        related_name='user_liked_series',
        null=True,
        blank=True,
    )
    watched_titles = models.ManyToManyField(
        'titles.Title',
        related_name='user_watched',
        null=True,
        blank=True,
    )

    def __str__(self):
        return self.username


class UserFollowing(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='following',
    )
    following = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='followers',
    )

    class Meta:
        unique_together = ('user', 'following')

    def __str__(self):
        return f'{self.user}: {self.following}'
