from users.apps import UsersConfig
from users.views import CustomUserViewSet, SubscriptionAPIView, SubscriptionRetrieveUpdateDestroyAPIView
from rest_framework.routers import DefaultRouter
from django.urls import path

app_name = UsersConfig.name

router = DefaultRouter()
router.register(r'', CustomUserViewSet, basename='users')

urlpatterns = [
    path('subscriptions/', SubscriptionAPIView.as_view(), name='subscriptions'),
    path('subscriptions/<int:pk>/', SubscriptionRetrieveUpdateDestroyAPIView.as_view()),
    ]
urlpatterns += router.urls
