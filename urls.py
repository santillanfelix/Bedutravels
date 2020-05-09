from django.contrib import admin
from django.urls import path, include  # modificada

urlpatterns = [
    path('', include("tours.urls")),  # agregada
    path('admin/', admin.site.urls),
]
