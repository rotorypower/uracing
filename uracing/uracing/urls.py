from django.conf import settings
from django.contrib import admin
from django.urls import path

from trackday.views import trackday_post
from uracing.views import register

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', trackday_post, name='home'),
    path('trackday/', trackday_post),
    path('register/', register),
]

if settings.DEBUG:
    from django.conf.urls.static import static
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns

    # Serve static and media files from development server
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)