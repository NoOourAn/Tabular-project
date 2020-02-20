from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('services/', include('services.url')),
    path('accounts/', include('accounts.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('contact/', include('contact.urls')),
<<<<<<< HEAD
    path('student/', views.student),
    path('about/', views.about),
=======
    path('student/', views.student ,name='student'),
>>>>>>> c285e37c0d85a53f95fad301e0350158016c8d6e
    path('',views.home, name='home'),


]
