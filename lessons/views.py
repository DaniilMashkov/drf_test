from rest_framework import generics
from rest_framework.mixins import RetrieveModelMixin, UpdateModelMixin
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from lessons.serializers import LessonSerializer
from lessons.models import Lesson
from config.permissions import ModeratorPermission


class LessonListView(RetrieveModelMixin, UpdateModelMixin, generics.ListAPIView):
    serializer_class = LessonSerializer
    permission_classes = [ModeratorPermission | IsAuthenticated]

    def get_queryset(self):
        if self.request.user.has_perm('lessons.change_lesson'):
            return Lesson.objects.all()
        else:
            user_lessons = self.request.user.payment_set.values_list('lesson_id')
            return Lesson.objects.filter(pk__in=user_lessons)

    def get(self, *args, **kwargs):
        if self.kwargs.get('pk'):
            return super().retrieve(*args, **kwargs)
        return super().list(*args, **kwargs)

    def patch(self, *args, **kwargs):
        return super().update(*args, **kwargs)


class LessonCreateAPIView(generics.CreateAPIView):
    serializer_class = LessonSerializer
    permission_classes = [IsAdminUser]


class LessonDestroyAPIView(generics.DestroyAPIView):
    serializer_class = LessonSerializer
    permission_classes = [IsAdminUser]
    queryset = Lesson.objects.all()
