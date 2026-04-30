from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    # Admin Django
    path('admin/', admin.site.urls),

    # Web (templates HTML)
    path('', include('core.urls')),

    # API REST propia
    path('api/', include('rest_api.urls')),

    # 🔐 Endpoint para obtener token (MUY IMPORTANTE)
    path('api/token/', obtain_auth_token, name='api_token_auth'),
]