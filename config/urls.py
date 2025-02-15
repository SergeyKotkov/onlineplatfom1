from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('electronics_network.urls')),  # Подключаем маршруты приложения network
]