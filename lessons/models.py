from django.db import models
from users.models import NULLABLE


class Lesson(models.Model):
    name = models.CharField(verbose_name='course_name', max_length=100)
    description = models.TextField(max_length=1000)
    preview = models.ImageField(upload_to='lessons/', **NULLABLE)
    link = models.CharField(verbose_name='video_link', max_length=254)

    class Meta:
        verbose_name = 'lesson'
        verbose_name_plural = 'lessons'
