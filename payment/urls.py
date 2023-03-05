from django.urls import path
from .views import PaymentStatusAPIView

urlpatterns = [
    path('status/', PaymentStatusAPIView.as_view(), name='purchase_status')
]