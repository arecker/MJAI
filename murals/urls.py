from django.conf.urls import include, url
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^contact/', include('contacting.urls')),
    url(r'^', include('showing.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
