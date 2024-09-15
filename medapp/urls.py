from django.urls import path
from . import views


urlpatterns=[path("",views.index,name="index"),
path("services/",views.services,name="services"),
path("contact/",views.contact,name="contact"),
path("blogs/",views.blogs,name="blogs"),
path("about/",views.about,name="about"),
path("detailblogs/",views.detailblogs,name="detailblogs"),
path("apppointment/",views.appointment,name="appointment"),





]

