from django.contrib import admin
from django.urls import path,include
from general.views import add_friend
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('general.urls')),
    path('',include('authentication.urls')),
    path('',include('blog.urls')),
    path('chat2/', include('chat.urls')),
    path('chat/', include('chat2.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)