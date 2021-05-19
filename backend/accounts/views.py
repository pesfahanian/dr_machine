from django.utils import timezone

from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from accounts.serializers import CustomUserSerializers, ProfileSerializers


class CustomUserView(APIView):
    permission_classes = (IsAuthenticated, )
    serializer_class = CustomUserSerializers

    def get(self, request, format=None):
        return Response(data=self.serializer_class(request.user).data,
                        status=status.HTTP_200_OK)


class LogoutView(APIView):
    permission_classes = (IsAuthenticated, )

    def get(self, request, format=None):
        user = request.user
        user.last_login = timezone.now()
        user.save()
        data = {"message": "user logged out successfully"}
        return Response(data=data, status=status.HTTP_200_OK)


class ProfileView(APIView):
    permission_classes = (IsAuthenticated, )
    serializer_class = ProfileSerializers

    def get(self, request, format=None):
        return Response(data=self.serializer_class(request.user).data,
                        status=status.HTTP_200_OK)
