from .views import *
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('login', LoginView, basename='login')
router.register('password', PasswordView, basename='password')
urlpatterns = router.urls

