from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q
from django.db.models import Count
#from .forms import ContactsForm
from .models import Paduka
from multiselectfield import MultiSelectField
#from apt.models import Appointment
from itertools import count
import operator


# Create your views here.

def index(request):
    return render(request, 'home/index.html')

#def jute_products_index(request):
#    return render(request, 'home/jute_products.html',)

def padukaindex(request):
    padukas = Paduka.objects.all()
    return render(request, 'home/paduka.html', {'padukas': padukas})

def strategy_index(request):
    return render(request, 'home/strategy.html',)

def eee_index(request):
    return render(request, 'home/eee.html',)

def contact_us(request):
    return render(request, 'home/contact_us.html',)
