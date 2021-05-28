from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

# Calling/Registering urls from all the projects 
urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('account.urls')),
    path('', include('appointment.urls')),
    path('', include('notes.urls')),
    path('', include('account.urls')),
    path('', include('dental_service.urls')),
    path('', include('doctors.urls')),
    path('', include('device_token.urls')),
    path('', include('time_table.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
