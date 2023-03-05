from rest_framework import serializers
from courses.models import Course, Subscription
from lessons.models import Lesson


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = ['name', ]


class CourseSerializer(serializers.ModelSerializer):
    total_lessons_count = serializers.SerializerMethodField()
    lessons = LessonSerializer(source='lesson_set', many=True, read_only=True)
    is_subscribed = serializers.SerializerMethodField()

    class Meta:
        model = Course
        fields = ['name', 'description', 'total_lessons_count', 'lessons', 'is_subscribed']
        ref_name = 'courses'

    def get_total_lessons_count(self, instance):
        return Lesson.objects.filter(course=instance.id).count()

    def get_is_subscribed(self, instance):

        if subscription := Subscription.objects.filter(course_id=instance.id):
            return subscription.first().status
        else:
            return None
