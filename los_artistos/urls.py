from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView

import artworks, users, homepage, artists, carts

urlpatterns = [
    path('admin/', admin.site.urls),
    path(r'concept/', TemplateView.as_view(template_name='concept.html'),name='concept'),
    path(r'artworks/', include('artworks.urls', namespace='artworks')),
    path(r'users/', include('users.urls', namespace='users')),
    path(r'artists/', include('artists.urls', namespace='artists')),
    path(r'carts/', include('carts.urls', namespace='carts')),
    path('', include ('homepage.urls')),
    path('', include('pwa.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
