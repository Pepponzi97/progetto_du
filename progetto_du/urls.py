# progetto_du/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('applicazione_du.urls')),  # Include le URL della tua applicazione
]