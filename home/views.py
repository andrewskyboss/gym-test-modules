"""
thecube_gym_fitness_club Home app view file
"""
from django.shortcuts import render, redirect
from .forms import ContactUsForm
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.contrib import messages


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
    form = ContactUsForm()
    
    if request.method == "POST":
    
        if form.is_valid():
            # subject = "Contact Us Gym Inquiry"
            email_address = request.POST['email_address']
            full_name = request.POST['full_name']
            message_field = request.POST['message_field']
            print("before send")

            # body = {
            #     'full_name': form.cleaned_data['full_name'],
            #     'email': form.cleaned_data['email_address'],
            #     'message': form.cleaned_data['message'],
            # }
            # message = "\n".join(body.values())

            try:
                # send_mail(subject, message, 'admin@example.com',
                #           ['admin@example.com'])
                send_mail(
                    'message from ' + full_name,
                    message_field,  # message
                    email_address,  # from email
                    ['thecubegym@gmail.com'],    
                )
                messages.success(request, f'Hey {full_name} Successfully received')
                print(send_mail(subject, message, from_email, recipient_list))
                
            except BadHeaderError:
                # messages.success(request, 'Successfully wrong.')
                return HttpResponse('Invalid header found.')
            return redirect("home/contact.html")
        
        print("wrong")
    else:
        return render(request, 'home/contact.html', {'form': form})
        print("wrong 1")

    return render(request, "home/contact.html", {'form': form})
