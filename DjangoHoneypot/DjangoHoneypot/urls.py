
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', include('admin_honeypot.urls')),

    path('pwnlab/', admin.site.urls),
]
