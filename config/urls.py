from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.urls import re_path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from config import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('contact.urls')),
    path('', include('home_page.urls')),
]

schema_view = get_schema_view(
    openapi.Info(
        title="Hackaton API",
        default_version='v1',
        description="Test description",
        terms_of_service="hackaton.com",
        contact=openapi.Contact(email="sunnat.akbarov0107@gmail.com"),
        license=openapi.License(name="Hackaton License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny, ],
)

urlpatterns += [
    path('swagger<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('doc/swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('doc/redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
