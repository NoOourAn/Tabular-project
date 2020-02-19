from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('services/', include('services.url')),
    path('accounts/', include('accounts.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('contact/', include('contact.urls')),
    path('student/', views.student ,name='student'),
    path('',views.home, name='home'),


]
