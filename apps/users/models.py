from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    bio = models.TextField(
        max_length=100,
    )
    avatar = models.ImageField(
        upload_to='user_avatar/',
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
    liked_title = models.ForeignKey(
        'titles.Title',
        on_delete=models.SET_NULL,
        related_name='user_liked_title',
        null=True,
        blank=True,
    )
    watched_titles = models.ManyToManyField(
        'titles.Title',
        related_name='user_watched',
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
