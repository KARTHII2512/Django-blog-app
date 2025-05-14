from django.contrib import admin
from django.urls import path, include
from blog import views as blog_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', blog_views.register, name='register'),
    path('', include('blog.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
]
