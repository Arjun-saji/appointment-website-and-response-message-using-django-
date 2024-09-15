from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
from .forms import *
from .twilio_service import send_sms

def index(request):
	services=Service.objects.all()
	blogs=Blog.objects.all()
	context={"services":services,"blogs":blogs}
	return render(request,'index.html',context)

def services(request):
	services=Service.objects.all()
	context={"services":services}
	return render(request,"service.html",context)

def contact(request):
	return render(request,"contact.html")


def blogs(request):
	blogs=Blog.objects.all()
	context={"blogs":blogs}
	return render(request,"blogs.html",context)

def detailblogs(request):
	blogs=Blog.objects.all()
	recent=Blog.objects.latest("created_date")
	context={"blogs":blogs,"recent":recent}
	return render(request,"detail_blogs.html",context)


def about(request):
	blogs=Blog.objects.all()
	context={"blogs":blogs}
	return render(request,"about.html",context)

def appointment(request):
	if request.method=="POST":
		forms=AppointmentForm(request.POST)
		if forms.is_valid:
			appointment=forms.save()
			message_body = (
				f"Dear {appointment.patient_name},\n"
				f"Your appointment has been successfully scheduled.\n"
				f"Service: {appointment.service}\n"
				f"Date: {appointment.appointment_date}\n"
				f"Phone: {appointment.phone}\n"
				f"Notes: {appointment.notes}\n"
				f"Thank you for choosing our service."
			)
			
			send_sms(appointment.phone, message_body)
			return redirect("index")
		else:
			print(forms.errors)
	else:
		forms=AppointmentForm()
	context={"forms":forms}


	return render(request,"appointment.html",context)







