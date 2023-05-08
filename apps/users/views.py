from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth import get_user_model, logout
from rest_framework import viewsets, generics, permissions, status, views
from rest_framework.authtoken.models import Token
from rest_framework.response import Response

from apps.users.serializers import UserSerializer, UserFollowBaseSerializer, LoginSerializer
from apps.users.models import UserFollowing
from utils.permissions import IsCurrentUser, IsOwnerUser

User = get_user_model()


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    search_fields = ('username',)
    permission_classes_by_action = {
        'list': [permissions.IsAuthenticated],
        'create': [permissions.AllowAny],
        'retrieve': [permissions.IsAuthenticated],
        'update': [permissions.IsAdminUser | IsCurrentUser],
        'delete': [permissions.IsAdminUser | IsCurrentUser],
    }

    def get_permissions(self):
        try:
            return [permission() for permission in self.permission_classes_by_action[self.action]]
        except KeyError:
            return [permission() for permission in self.permission_classes]

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context.update({"request": self.request})
        return context


class FollowUserAPIView(generics.CreateAPIView):
    queryset = UserFollowing.objects.all()
    serializer_class = UserFollowBaseSerializer

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context.update({"request": self.request})
        return context

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class UnfollowUserAPIView(generics.GenericAPIView):
    queryset = UserFollowing.objects.all()
    serializer_class = UserFollowBaseSerializer
    permission_classes = (IsOwnerUser,)

    def post(self, request):
        serializer = self.serializer_class(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        unfollow_user = serializer.validated_data['following']
        try:
            UserFollowing.objects.get(user=self.request.user, following=unfollow_user).delete()
            return Response({
                'messsage': f'You unfollowed {unfollow_user}'
            })
        except ObjectDoesNotExist:
            return Response({
                'message': f'You are not followed to {unfollow_user}'
            })


class TokenLoginAPIView(generics.GenericAPIView):
    serializer_class = LoginSerializer
    permission_classes = (permissions.AllowAny,)

    def post(self, request):
        serializer = self.serializer_class(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'status': 1 if user.is_superuser else 2,
            'id': user.id,
            'username': user.username,
            'email': user.email,
            'bio': user.bio,
            'avatar': f'{request.build_absolute_uri().replace("/user/token/create/", "")}{user.avatar.url}',
            'liked_actor': user.liked_actor.id if user.liked_actor else None,
            'liked_title': user.liked_title.id if user.liked_title else None,
            'liked_director': user.liked_director.id if user.liked_director else None,
            'watched_titles': [wt.id for wt in user.watched_titles.all()],
        })


class TokenLogoutAPIView(views.APIView):
    def post(self, request):
        return self.logout(request)

    def logout(self, request):
        try:
            request.user.auth_token.delete()
        except (AttributeError, ObjectDoesNotExist):
            pass
        logout(request)
        return Response({"success": "Successfully logged out."}, status=status.HTTP_200_OK)
