from django.shortcuts import render
from formtools.wizard.views import SessionWizardView
from django.conf import settings
from django.core.files.storage import FileSystemStorage

# Create your views here.
def step1(request):
    return render(request, 'services/manual-data.html')

def step2(request):
    return render(request , 'services/excel-sheet.html')

def step3(request):
    return render(request, 'services/generated-timetable.html')

def home(request):
    return render(request, 'services/home.html')

class DataWizard(SessionWizardView):
    file_storage = FileSystemStorage(settings.MEDIA_ROOT)
    template_name = "services/manual-data.html"
    def done(self, form_list, **kwargs):
        form_data = [form.cleaned_data for form in form_list]
        return render(self.request, 'services/generated-timetable.html', {'form_data': form_data})
