from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('user_profile.urls')),
    path('buyers/', include('buyer.urls')),
    path('inv/', include('invoice.urls'))
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
