from django.core.management import BaseCommand
from django_celery_beat.models import PeriodicTask, IntervalSchedule


class Command(BaseCommand):

    def handle(self, *args, **options):
        schedule, created = IntervalSchedule.objects.get_or_create(
            every=10,
            period=IntervalSchedule.SECONDS,
        )
        PeriodicTask.objects.create(
            interval=schedule,
            name='check payment status',
            task='payment.tasks.check_payment_status',

        )