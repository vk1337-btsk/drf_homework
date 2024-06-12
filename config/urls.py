from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('apps.users.urls', namespace='users')),
    path('', include('apps.materials.urls', namespace='materials')),
]
