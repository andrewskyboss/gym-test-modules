"""
thecube_gym_fitness_club Home app view file
"""
from django.shortcuts import render


# Create your views here.


def index(request):
    """ A view for index page """
    return render(request, 'home/index.html')


def activities(request):
    """ A view for activities page """
    return render(request, 'home/activities.html')


def contact(request):
    """ A view for coaches page """
    return render(request, 'home/contact.html')


def gym(request):
    """ A view for gym page """
    return render(request, 'home/gym.html')


def timetable(request):
    """ A view for timetable page """
    return render(request, 'home/timetable.html')
