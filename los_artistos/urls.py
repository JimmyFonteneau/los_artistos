from django.contrib import admin
from django.urls import path, include

import artworks, users, homepage

urlpatterns = [
    path('admin/', admin.site.urls),
    path(r'artworks/', include('artworks.urls', namespace='artworks')),
    path(r'users/', include('users.urls', namespace='users')),
    path('', include ('homepage.urls')),
    path('', include('pwa.urls')),
]
