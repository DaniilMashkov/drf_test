from users.apps import UsersConfig
from users.views import CustomUserViewSet
from rest_framework.routers import DefaultRouter


app_name = UsersConfig.name

router = DefaultRouter()
router.register(r'', CustomUserViewSet, basename='users')

urlpatterns = [] + router.urls