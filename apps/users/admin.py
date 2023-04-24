from django.contrib import admin
from django.contrib.auth import get_user_model

from apps.users.models import UserFollowing

User = get_user_model()


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'date_joined')
    list_display_links = ('id', 'username', 'date_joined')
    list_filter = ('id', 'date_joined')
    search_fields = ('id', 'username')


@admin.register(UserFollowing)
class UserFollowingAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'following')
    list_display_links = ('id', 'user')
    list_filter = ('id', 'user', 'following')
    search_fields = ('id', 'user', 'following')

