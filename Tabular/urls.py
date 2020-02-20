from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('services/', include('services.url')),
    path('accounts/', include('accounts.urls')),
    path('contact/', include('contact.urls')),
    path('student/', views.student),
    path('about/', views.about),
    path('',views.home, name='home'),
]
