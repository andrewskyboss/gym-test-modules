"""
thecube_gym_fitness_club Home app view file
"""
from django.shortcuts import render, redirect
from django.core.mail import send_mail, BadHeaderError
from django.core.mail import EmailMessage
from django.http import HttpResponse
from django.contrib import messages
from django.template.loader import get_template
from .forms import ContactUsForm


# Create your views here.


def index(request):
    """ A view for index page """
    return render(request, 'home/index.html')


def activities(request):
    """ A view for activities page """
    return render(request, 'home/activities.html')


# def contact(request):
#     """ A view for coaches page """
#     return render(request, 'home/contact.html')


def gym(request):
    """ A view for gym page """
    return render(request, 'home/gym.html')


def timetable(request):
    """ A view for timetable page """
    return render(request, 'home/timetable.html')


def contact(request):
    # form = ContactUsForm()
    form_class = ContactUsForm

    if request.method == "POST":

        form = form_class(data=request.POST)

        if form.is_valid():
            # subject = "Contact Us Gym Inquiry"

            email_address = request.POST.get('email_address', '')
            full_name = request.POST.get('full_name', '')
            message_field = request.POST.get('message_field', '')
            print("---------------------before send")

            # body = {
            #     'full_name': form.cleaned_data['full_name'],
            #     'email': form.cleaned_data['email_address'],
            #     'message': form.cleaned_data['message'],
            # }
            # message = "\n".join(body.values())

            try:
                # send_mail(subject, message, 'admin@example.com',
                #           ['admin@example.com'])
                # send_mail(
                #     'message from ' + full_name,
                #     message_field,
                #     email_address,
                #     ['thecubegym@gmail.com'],
                # )

                template = get_template('contact_template.txt')
                context = {
                    'email_address': email_address,
                    'full_name': full_name,
                    'message_field': message_field,
                }
                content = template.render(context)
                recipients = ['contact@thecubegym.com']

                message = EmailMessage(
                    "New contact form submission",
                    content,
                    "Your website", ['contact@thecubegym.com'],
                    headers={'Reply-To': email_address}
                )
                # email.send()
                send_mail(full_name, str(message), email_address, recipients)
                form.save()
                messages.success(
                    request, f'Hey {full_name} Successfully received')

                print("----------------------- sent process")
                return redirect('home')

            except BadHeaderError:
                messages.success(request, 'Successfully wrong.')
                # return HttpResponse('Invalid header found.')
                return redirect("home/contact.html")

            print("wrong")
    else:
        return render(request, 'home/contact.html', {'form': form_class})
        print("wrong 1")

    return render(request, "home/contact.html", {'form': form_class})
