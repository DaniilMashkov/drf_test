from django.db import models
from users.models import NULLABLE
from courses.models import Course


class Lesson(models.Model):
    name = models.CharField(verbose_name='course_name', max_length=100)
    description = models.TextField(max_length=1000)
    preview = models.ImageField(upload_to='lessons/', **NULLABLE)
    link = models.URLField(verbose_name='video_link')
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'lesson'
        verbose_name_plural = 'lessons'
