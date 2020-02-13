from django.shortcuts import render
from formtools.wizard.views import SessionWizardView
from django.core.files.storage import FileSystemStorage

# from services import forms

# Create your views here.
def step1(request):
    return render(request, 'services/manual-data.html')

def step2(request):
    return render(request , 'services/excel-sheet.html')

def step3(request):
    return render(request, 'services/generated-timetable.html')

def home(request):
    return render(request, 'services/home.html')


# FORMS = [("manualdata", forms.ManualData),
#          ("timeslots", forms.TimeSlots),
#          ("excelsheet", forms.ExcelSheet)]
#
# TEMPLATES = {"manualdata": "services/manual-data.html",
#              "timeslots": "services/time-slots.html",
#              "excelsheet": "services/excel-sheet.html"}
#
# def count_days(wizard):
#     cleaned_data = wizard.get_cleaned_data_for_step('manualdata') or {'method': 'none'}
#     days = cleaned_data['duedate'] - cleaned_data['startdate']
#     return days


class DataWizard(SessionWizardView):
    file_storage = FileSystemStorage(location='/media/files')
    template_name = "services/manual-data.html"

    # def get_template_name(self):
    #     return [TEMPLATES[self.steps.current]]

    def done(self, form_list, **kwargs):
        form_data = [form.cleaned_data for form in form_list]
        return render(self.request, 'services/generated-timetable.html', {'form_data': form_data})
