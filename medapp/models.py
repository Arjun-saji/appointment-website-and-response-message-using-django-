from django.db import models
from django.utils import timezone


class Service(models.Model):
	title=models.CharField(max_length=200)
	description=models.TextField()
	pic=models.ImageField(upload_to='images/',blank=True,null=True)

	def __str__(self):
		return self.title

class Appointment(models.Model):
	patient_name=models.CharField(max_length=100)
	service=models.ForeignKey(Service,on_delete=models.CASCADE)
	appointment_date=models.DateTimeField()
	email=models.EmailField()
	phone=models.CharField(max_length=15)
	notes=models.TextField()

	def __str__(self):
		return self.patient_name

class Blog(models.Model):
	blog_title=models.CharField(max_length=300)
	blog_desc=models.TextField()
	created_date=models.DateTimeField(default=timezone.now)
	blog_img=models.ImageField(upload_to='images/',blank=True,null=True)

	def __str__(self):
		return self.blog_title






