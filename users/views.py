from rest_framework import viewsets
from users.serializers import CustomUserSerializer, CustomUser


class CustomUserViewSet(viewsets.ModelViewSet):
    serializer_class = CustomUserSerializer
    queryset = CustomUser.objects.all()
