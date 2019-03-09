from django.shortcuts import render, get_object_or_404, redirect
from datetime import datetime
from django.contrib import messages
from django.db.models import Q
from .models import Appartments, Booking

# Create your views here.
def homeView(request):
    myDate = datetime.now()
    context = {
        'date': myDate,
    }
    return render(request, 'apartment/home.html', context)

def about_us(request):
    myDate = datetime.now()
    context = {
        'date': myDate,
    }
    return render(request, 'apartment/about.html', context)


def contact_us(request):
    myDate = datetime.now()
    context = {
        'date': myDate,
    }
    return render(request, 'apartment/contact.html', context)


def appartmentView(request):
    get_appartment = Appartments.objects.all().order_by('-id')
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
def bookingDeatails(request, slug):
    if request.method == "POST":
        firstname = request.POST.get('fname')
        lastname = request.POST.get('lname')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        datein = request.POST.get('datein')
        dateout = request.POST.get('dateout')
        booking_object = Booking(first_name = firstname, last_name = lastname, email_address = email, phone_number = phone, check_in = datein, check_out = dateout)
        booking_object.save()
        messages.success(request, 'Your booking is done successfuly..!')
        return redirect('/bookingDeatails/')
    else:    
        get_appartment_detail = get_object_or_404(Appartments, slug = slug)
        myDate = datetime.now()
        context = {
            'date':myDate,
            'appartment_details':get_appartment_detail
        }
        return render(request, 'apartment/booking.html', context)
