from rest_framework import serializers
from users.models import CustomUser
from payment.models import Payment


class PaymentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Payment
        fields = ('amount', 'course', 'lesson')


class CustomUserSerializer(serializers.ModelSerializer):
    payments = PaymentSerializer(source='payment_set', many=True)

    class Meta:
        model = CustomUser
        fields = ('email', 'password', 'avatar', 'phone', 'city', 'payments')


class ForeignUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('email', 'avatar', 'phone', 'city')