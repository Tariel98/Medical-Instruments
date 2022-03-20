from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render
from .forms import ContactForm
from Instruments.models import Partner


def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        massage = ''
        if form.is_valid():
            form.save()

            try:
                email_subject = f'New contact {form.cleaned_data["email"]}: {form.cleaned_data["subject"]}'
                email_message = form.cleaned_data['message']
                send_mail(email_subject, email_message, settings.CONTACT_EMAIL, settings.ADMIN_EMAILS)

            except:
                massage += "Ձեր հաղորդագրությունը չի ուղարկվել"
            else:
                email_subject = 'Ծանուցում'
                email_message = 'Մենք ստացել ենք Ձեր նամակը։\n Շուտով մեր աշխատակիցը կպատասխանի Ձեզ։'
                send_mail(email_subject, email_message, settings.CONTACT_EMAIL, [form.cleaned_data['email']])
                print(form.cleaned_data['email'])
                massage +='Մենք ստացել ենք Ձեր նամակը'
            return render(request, 'Instruments/../templates/ContactUs/contact.html', {'massage': massage})

        else:
            print(form.errors)
            for i in form.errors:
                massage += form.errors[i]
            return render(request, 'Instruments/../templates/ContactUs/contact.html', {'massage': massage})
    form = ContactForm()
    context = {'form': form, 'parters': Partner.objects.filter(status='p')}
    return render(request, 'Instruments/../templates/ContactUs/contact.html', context)




