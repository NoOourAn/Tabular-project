from django.urls import path
from . import views

from django.conf.urls import url
# from services.forms import ManualData, TimeSlots,ExcelSheet
# from services.views import DataWizard

urlpatterns = [
    path('', views.home, name='serviceshome'),

    path('manual-data', views.step1 , name='manualdata'),
    path('timeslots', views.step2, name='timeslots'),

    # path('timetable', views.step3, name='timetable'),
    # path('timetable/<str:tt_id>', views.step3, name='timetable'),

    path('excel-sheet', views.step3, name='excelsheet'),
    path('timetable', views.step4, name='timetable'),

    path('dashboard', views.fetchTT, name='dashboard'),
    path('TT', views.fetchOneTT, name='TT'),

    path('boom', views.boom, name='boom'),
    path('pdf', views.create_pdf, name='pdf'),

    # url('data', DataWizard.as_view([ManualData, TimeSlots , ExcelSheet]) ,  name='data'),

]
