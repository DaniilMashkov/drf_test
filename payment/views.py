from rest_framework.views import APIView
from payment.models import Payment
from django.http import JsonResponse
from rest_framework.response import Response
import requests
from django.conf import settings
from hashlib import sha256
import json


class PaymentAPIView(APIView):

    def get(self, *args, **kwargs):
        payment_instance = Payment.objects.create(
            amount=140000, method='transfer', user_id=self.request.user.pk)

        data_for_hash = str(payment_instance.amount) + str(payment_instance.pk) + \
                        settings.TINKOFF_PASSWORD + settings.TINKOFF_TERMINAL_KEY
        hash_key = sha256(data_for_hash.encode('utf-8')).hexdigest()

        request_data = {
            "TerminalKey": settings.TINKOFF_TERMINAL_KEY,
            "Amount": payment_instance.amount,
            "OrderId": payment_instance.pk,
        }
        r = requests.post('https://securepay.tinkoff.ru/v2/Init',
                          json.dumps(request_data), headers={'Content-type': 'application/json'})

        payment_instance.hash_key = hash_key
        payment_instance.status = r.json()['Status']
        payment_instance.purchase_id = r.json()['PaymentId']
        payment_instance.save()

        return Response(r.json())


class PaymentStatusAPIView(APIView):

    def get(self, *args, **kwargs):

        payments = Payment.objects.filter(status='NEW')

        for payment in payments:

            request_data = {
                "TerminalKey": settings.TINKOFF_TERMINAL_KEY,
                "PaymentId": payment.purchase_id,
                "Token": payment.hash_key
            }

            r = requests.post('https://securepay.tinkoff.ru/v2/GetState',
                              json.dumps(request_data), headers={'Content-type': 'application/json'})

            if r.json().get('Success'):
                payment.status = r.json().get('Status')
                payment.save()

        payments_values = list(payments.values())

        return JsonResponse(payments_values, safe=False)
