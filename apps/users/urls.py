from rest_framework.routers import DefaultRouter
from apps.users.apps import UsersConfig
from apps.users.views import UserViewSet

app_name = UsersConfig.name

router = DefaultRouter()
router.register(r'users', UserViewSet, basename='users')

urlpatterns = router.urls