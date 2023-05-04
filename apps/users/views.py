from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth import get_user_model, logout
from rest_framework import viewsets, generics, permissions, status, views
from rest_framework.authtoken.models import Token
from rest_framework.response import Response

from apps.users.serializers import UserSerializer, UserFollowingSerializer, LoginSerializer
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


class FollowUserAPIView(generics.CreateAPIView):
    queryset = UserFollowing.objects.all()
    serializer_class = UserFollowingSerializer


class UnfollowUserAPIView(generics.DestroyAPIView):
    queryset = UserFollowing.objects.all()
    serializer_class = UserFollowingSerializer
    permission_classes = (IsOwnerUser,)


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
            'user_id': user.id,
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
