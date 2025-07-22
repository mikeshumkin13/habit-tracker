from rest_framework import generics, permissions
from .serializers import UserRegistrationSerializer
from django.contrib.auth import get_user_model


User = get_user_model()


class RegisterAPIView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserRegistrationSerializer
    permission_classes = [permissions.AllowAny]



