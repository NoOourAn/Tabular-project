from django.urls import path , include
from . import views
urlpatterns = [
    path('signup/', views.signup , name='signup'),
    path('signupp/', views.signupp, name='signupp'),
    path('signupoo/', views.signupoo, name='signupoo'),

    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('osignup/', views.osignup, name='osignup'),
    path('reg/', views.reg , name='reg'),
    path('reg2/', views.reg2, name='reg2'),
]
