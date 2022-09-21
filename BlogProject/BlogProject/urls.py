from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

""" Aquí se importan todos los links de aplicaciones que se han hecho aparte como members """
urlpatterns = [
    path("admin/", admin.site.urls),
    path('', include('main.urls')),
    path('members/', include('django.contrib.auth.urls')),
    path('members/', include('members.urls')),

]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)