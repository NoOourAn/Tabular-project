from django.shortcuts import render, redirect
from .models import Contact
from django.core.mail import send_mail


def index(request):
    if request.method == 'POST':
        contact = Contact()
        contact.FirstName = request.POST['firstname']
        contact.LastName = request.POST['lastname']
        contact.Email = request.POST['email']
        contact.TelephoneNumber = request.POST['telephonenumber']
        contact.Country = request.POST['country']
        contact.Message = request.POST['message']

        contact.save()

        try:
            send_mail(
                contact.FirstName,
                contact.Message,
                'johnny.magdy18@gmail.com',
                ['j.magdy18@yahoo.com'],
                fail_silently=False,
            )
        except ConnectionRefusedError:
            pass

        return render(request, 'contact/index.html', {'Success': 'Message sent successfully'})
    else:
        return render(request, 'contact/index.html')
