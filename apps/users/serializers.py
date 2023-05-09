from rest_framework import serializers
from django.contrib.auth import get_user_model, authenticate

from apps.users.models import UserFollowing

User = get_user_model()


class UserFollowBaseSerializer(serializers.ModelSerializer):
    user = serializers.CharField(read_only=True)

    class Meta:
        model = UserFollowing
        fields = (
            'id',
            'user',
            'following',
        )


class UserFollowingSerializer(serializers.ModelSerializer):
    following = serializers.SerializerMethodField()

    class Meta:
        model = UserFollowing
        fields = (
            'id',
            'following',
        )

    def get_following(self, obj):
        user = obj.following
        return {
            'id': user.id,
            'username': user.username,
            'avatar': user.avatar.url,
        }


class UserFollowerSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()

    class Meta:
        model = UserFollowing
        fields = (
            'id',
            'user',
        )

    def get_user(self, obj):
        user = obj.user
        return {
            'id': user.id,
            'username': user.username,
            'avatar': user.avatar.url,
        }


class UserSerializer(serializers.ModelSerializer):
    following = UserFollowingSerializer(many=True, read_only=True)
    followers = serializers.SerializerMethodField()
    avatar = serializers.ImageField(required=False)

    class Meta:
        model = User
        fields = (
            'id',
            'username',
            'email',
            'bio',
            'avatar',
            'liked_actor',
            'liked_film',
            'liked_series',
            'liked_director',
            'watched_titles',
            'following',
            'followers',
            'password',
        )

    def create(self, validated_data):
        if not validated_data['password']:
            raise serializers.ValidationError('Password can\'t be null!')
        watched_titles = validated_data['watched_titles']
        validated_data.pop('watched_titles')
        user = User(**validated_data)
        user.set_password(validated_data['password'])
        user.save()
        user.watched_titles.set(watched_titles)
        return user

    def get_followers(self, obj):
        followers = obj.followers.all()
        serializer = UserFollowerSerializer(followers, many=True)
        return serializer.data


class UserUpdatePasswordSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'id',
            'password',
        )

    def update(self, instance, validated_data):
        instance.set_password(validated_data['password'])
        instance.save()
        return instance


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(
        write_only=True
    )
    password = serializers.CharField(
        style={'input_type': 'password'},
        trim_whitespace=False,
        write_only=True
    )
    token = serializers.CharField(
        label="Token",
        read_only=True
    )

    def validate(self, attrs):
        username = attrs.get('username')
        password = attrs.get('password')

        if username and password:
            user = authenticate(request=self.context.get('request'), username=username, password=password)

            if not user:
                msg = 'Unable to log in with provided credentials.'
                raise serializers.ValidationError(msg, code='authorization')
        else:
            msg = 'Must include "username" and "password".'
            raise serializers.ValidationError(msg, code='authorization')
        attrs['user'] = user
        return attrs
