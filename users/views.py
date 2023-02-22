from rest_framework import viewsets
from users.serializers import CustomUserSerializer, CustomUser, ForeignUserSerializer
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from config.permissions import ProfilePermission


class CustomUserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()

    def get_permissions(self):

        if self.action == 'list':
            permission_classes = [IsAuthenticated]
        if self.action == 'update':
            permission_classes = [ProfilePermission]
        if self.action == 'partial_update':
            permission_classes = [ProfilePermission]
        if self.action == 'retrieve':
            permission_classes = [IsAuthenticated]
        if self.action == 'destroy':
            permission_classes = [IsAdminUser]
        if self.action == 'create':
            permission_classes = [IsAdminUser]

        return [permission() for permission in permission_classes]

    def get_serializer_class(self, **kwargs):
        if self.kwargs.get('pk') == str(self.request.user.pk):
            return CustomUserSerializer
        else:
            return ForeignUserSerializer
