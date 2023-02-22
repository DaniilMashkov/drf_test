from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, IsAdminUser

from courses.serializers import CourseSerializer
from courses.models import Course
from config.permissions import ModeratorPermission


class CourseViewSet(viewsets.ModelViewSet):
    serializer_class = CourseSerializer

    def get_permissions(self):

        if self.action == 'list':
            permission_classes = [ModeratorPermission | IsAuthenticated]
        if self.action == 'update':
            permission_classes = [ModeratorPermission | IsAuthenticated]
        if self.action == 'partial_update':
            permission_classes = [ModeratorPermission | IsAuthenticated]
        if self.action == 'retrieve':
            permission_classes = [ModeratorPermission | IsAuthenticated]
        if self.action == 'destroy':
            permission_classes = [IsAdminUser]
        if self.action == 'create':
            permission_classes = [IsAdminUser]

        return [permission() for permission in permission_classes]

    def get_queryset(self):
        if self.request.user.has_perm('courses.change_course'):
            return Course.objects.all()
        else:
            user_courses = self.request.user.payment_set.values_list('course_id')
            return Course.objects.filter(pk__in=user_courses)
