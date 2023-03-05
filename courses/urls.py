from rest_framework.routers import DefaultRouter
from courses.views import CourseViewSet
from django.urls import path
from payment.views import PaymentAPIView, PaymentStatusAPIView

router = DefaultRouter()
router.register(r'', CourseViewSet, basename='course')

urlpatterns = [
    path('<int:pk>/purchase/', PaymentAPIView.as_view(), name='purchase'),
    # path('<int:pk>/purchase/status/', PaymentStatusAPIView.as_view(), name='purchase_status')
]

urlpatterns += router.urls