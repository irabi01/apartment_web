from django.shortcuts import render, get_object_or_404, redirect
from datetime import datetime
from django.contrib import messages
from django.db.models import Q
from .models import Appartments

# Create your views here.
def homeView(request):
    myDate = datetime.now()
    context = {
        'date': myDate,
    }
    return render(request, 'apartment/home.html', context)
def appartmentView(request):
    get_appartment = Appartments.objects.all()
    myDate = datetime.now()
    context = {
        'date':myDate,
        'appartments':get_appartment
    }
    return render(request, 'apartment/apartment.html', context)

def appartmentDetailView(request, slug):
    get_appartment_detail = get_object_or_404(Appartments, slug = slug)
    myDate = datetime.now()
    context = {
        'date':myDate,
        'appartment_details':get_appartment_detail
    }
    return render(request, 'apartment/details.html', context)
