from rest_framework import serializers
from lessons.models import Lesson
from config.validators import LinkValidator


class LessonSerializer(serializers.ModelSerializer):

    class Meta:
        model = Lesson
        fields = ('name', 'description', 'preview', 'link', 'course')
        validators = [LinkValidator(field='model')]
        ref_name = 'lessons'
