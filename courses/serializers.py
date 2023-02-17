from rest_framework import serializers
from courses.models import Course
from lessons.models import Lesson


class LessonSerializer(serializers.ModelSerializer):

    class Meta:
        model = Lesson
        fields = ['name', ]


class CourseSerializer(serializers.ModelSerializer):
    total_lessons_count = serializers.SerializerMethodField()
    lessons = LessonSerializer(source='lesson_set', many=True)

    class Meta:
        model = Course
        fields = ['name', 'preview', 'description', 'total_lessons_count', 'lessons']

    def get_total_lessons_count(self, instance):
        return Lesson.objects.filter(course=instance.id).count()