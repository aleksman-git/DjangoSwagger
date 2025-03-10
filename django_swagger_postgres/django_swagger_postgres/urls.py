from django.urls import path
from django.urls import include
from django.contrib import admin
from drf_spectacular.views import SpectacularAPIView
from drf_spectacular.views import SpectacularRedocView
from drf_spectacular.views import SpectacularSwaggerView


urlpatterns = [
    path('admin/', admin.site.urls),
    path("",include("django_app.urls")),
    path('schema/', SpectacularAPIView.as_view(), name='schema'),
    path('redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
    path('swagger/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
]
