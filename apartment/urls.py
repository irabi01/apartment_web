from django.urls import path, include
from django.conf.urls import url
from . import views

urlpatterns = [
    path('', views.homeView, name = "home"),
    path('about_us/', views.about_us, name = "about_us"),
    path('contact_us/', views.contact_us, name = "contact_us"),
    path('appartments/', views.appartmentView, name = "appartments"),
    url(r'^appartments/(?P<slug>[\w-]+)/details/$', views.appartmentDetailView, name = "appartmentsDetail"),
    url(r'^appartments/(?P<slug>[\w-]+)/details/booking/$', views.bookingDeatails, name = "bookingDeatails"),
]
