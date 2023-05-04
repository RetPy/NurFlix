from rest_framework import serializers
from django.contrib.auth import get_user_model, authenticate

from apps.users.models import UserFollowing

User = get_user_model()


class UserFollowingSerializer(serializers.ModelSerializer):
    user = serializers.CharField(read_only=True)

    class Meta:
        model = UserFollowing
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    followings = UserFollowingSerializer(many=True, read_only=True)
    followers = UserFollowingSerializer(many=True, read_only=True)
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
            'liked_title',
            'liked_director',
            'watched_titles',
            'followings',
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
