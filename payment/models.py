from django.db import models
from users.models import CustomUser, NULLABLE
from courses.models import Course
from lessons.models import Lesson


payment_methods = (('cash', 'Cash'), ('transfer', 'Transfer'))


class Payment(models.Model):
    date = models.DateTimeField(auto_now=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    method = models.CharField(choices=payment_methods, max_length=30)

    user = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, **NULLABLE)
    course = models.ForeignKey(Course, on_delete=models.SET_NULL, **NULLABLE)
    lesson = models.ForeignKey(Lesson, on_delete=models.SET_NULL, **NULLABLE)
