from django.core.management import BaseCommand
from payment.models import Payment


class Command(BaseCommand):
    def handle(self, *args, **options):

        payment_list = [
            Payment(user_id=1,
                    amount=999.99,
                    method='transfer',
                    course_id=1
                    ),
            Payment(user_id=1,
                    amount=1.11,
                    method='cash',
                    lesson_id=1
                    )
        ]
        Payment.objects.bulk_create(payment_list)