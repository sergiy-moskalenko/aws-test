from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularSwaggerView,
    SpectacularRedocView
)

from . import views

# from core.settings.base import MEDIA_ROOT, MEDIA_URL
# from django.views.generic import RedirectView

urlpatterns = [
    path("", views.TestAPI.as_view()),
    path('admin/', admin.site.urls),
    # path('__debug__/', include('debug_toolbar.urls')),
    # drf_spectacular
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/doc/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    # path('', RedirectView.as_view(url='api/doc/', permanent=False), name='root-redirect'),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
