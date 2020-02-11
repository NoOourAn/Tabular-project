from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='serviceshome'),
    path('manual-data', views.step1 , name='manualdata'),
    path('excel-sheet', views.step2, name='excelsheet'),
    path('timetable', views.step3, name='timetable'),
]
