from django.db import models

class Student(models.Model):
	first_name = models.CharField(max_length=50)
	last_name = models.CharField(max_length=50)
	date_of_birth = models.DateField()
	registration_number = models.CharField(max_length=50)
	place_of_residence = models.CharField(max_length=50)
	phone_number = models.CharField(max_length=50)
	email = models.CharField()
	guardian_name = models.CharField(max_length=50)
	id_number = models.CharField(max_length=50)
	date_joined = models.integerField()
		
