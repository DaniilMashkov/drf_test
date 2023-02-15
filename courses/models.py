from django.db import models
from users.models import NULLABLE


class Course(models.Model):
    name = models.CharField(verbose_name='course_name', max_length=100)
    preview = models.ImageField(upload_to='courses/', **NULLABLE)
    description = models.TextField(max_length=1000)

    class Meta:
        verbose_name = 'course'
        verbose_name_plural = 'courses'
