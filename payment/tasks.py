import requests
from django.core.mail import send_mail
from celery import shared_task
from courses.models import Course, Subscription
from users.models import CustomUser
from django.conf.global_settings import EMAIL_HOST_USER


def check_payment_status():
    return requests.get('payments/status/')


@shared_task
def notify_if_course_content_changed(course_pk):

    subscriptions = Subscription.objects.filter(course_id=course_pk, status=True)
    subscribed_users = CustomUser.objects.filter(pk__in=subscriptions.values_list('user_id'))
    users_emails = list(subscribed_users.values_list('email'))[0]
    course_obj = Course.objects.get(pk=course_pk)

    send_mail(
        subject='New content',
        message=f'Course {course_obj.name} has been changed',
        from_email=EMAIL_HOST_USER,
        recipient_list=users_emails
    )


