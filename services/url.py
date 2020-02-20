from django.urls import path
from . import views

from django.conf.urls import url
from services.forms import ManualData, TimeSlots,ExcelSheet
from services.views import DataWizard

urlpatterns = [
    path('', views.home, name='serviceshome'),
    path('manual-data', views.step1 , name='manualdata'),
    path('excel-sheet', views.step2, name='excelsheet'),
    path('timetable/<str:tt_id>', views.step3, name='timetable'),

    url('data', DataWizard.as_view([ManualData, TimeSlots , ExcelSheet]) ,  name='data'),

]
