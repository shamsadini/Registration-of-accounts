# sabte_shams/urls.py

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounting/', include('accounting.urls')),
    path('api/', include('accounting.urls')),  # ثبت آدرس‌های API
]
