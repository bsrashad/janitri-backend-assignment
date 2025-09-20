from rest_framework import generics
from .models import User
from .serializers import UserRegisterSerializer
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView


class UserRegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserRegisterSerializer
    permission_classes = [AllowAny]
