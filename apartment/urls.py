from django.urls import path, include
from django.conf.urls import url
from . import views

urlpatterns = [
    path('', views.homeView, name = "home"),
    path('appartments/', views.appartmentView, name = "appartments"),
    url(r'^appartments/(?P<slug>[\w-]+)/details/$', views.appartmentDetailView, name = "appartmentsDetail"),
]
