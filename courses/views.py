from rest_framework import viewsets
from courses.serializers import CourseSerializer
from courses.models import Course


class CourseViewSet(viewsets.ModelViewSet):
    serializer_class = CourseSerializer
    queryset = Course.objects.all()
