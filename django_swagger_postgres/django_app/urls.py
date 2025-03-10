from rest_framework.routers import DefaultRouter

from .views import LoginViewSet


router = DefaultRouter()
router.register('login', LoginViewSet, basename='login')
#router.register('password', PasswordView, basename='password')
urlpatterns = router.urls

