from django.db import models
from phone_field import PhoneField
from django.utils import timezone
from django.core.validators import RegexValidator
from django.core.validators import MaxValueValidator , MinValueValidator

BLOOD_GROUPS = (
        ('A+', 'A+'),
        ('A-', 'A-'),
        ('B+', 'B+'),
        ('B-', 'B-'),
        ('AB+', 'AB+'),
        ('AB-', 'AB-'),
        ('O+', 'O+'),
        ('O-', 'O-'),
    )
GENDER = (
		('Male', 'Male'),
		('Female', 'Female'),
		('Other', 'Other'),
	)

LOCATION = (
		('Kathmandu', 'Kathmandu'),
		('Bhaktapur', 'Bhaktapur'),
		('Lalitpur', 'Lalitpur'),
		('Birtamod', 'Birtamod'),
		('Pokhara', 'Pokhara'),
	)

class Donor(models.Model):
	name = models.CharField(max_length= 75)
	age = models.PositiveIntegerField(validators=[MinValueValidator(17), MaxValueValidator(70)])
	gender = models.CharField(max_length=7, choices=GENDER)
	phone = models.CharField(max_length=15, validators=[RegexValidator(r'^\d{1,15}$')], null=False, blank=False, unique=True,)
	bloodgroup = models.CharField(max_length=5, choices=BLOOD_GROUPS)
	location = models.CharField(max_length=50, choices=LOCATION)
	verified = models.BooleanField(default=False)	
	date_joined = models.DateTimeField(default=timezone.now)

	def __str__(self):
		return self.name

class Blood(models.Model):
	bloodgroup = models.CharField(max_length=5, choices=BLOOD_GROUPS)
	amount = models.PositiveIntegerField(null=False, blank=False)
	donate_date = models.DateField(auto_now=False, auto_now_add=False)
	expiry_date = models.DateField(null=False, blank=False)

	def __str__(self):
		return self.bloodgroup



class Contact(models.Model):
	name= models.CharField(max_length=75)
	email = models.EmailField()
	message = models.TextField()
	date_posted = models.DateTimeField(default=timezone.now)



	def __str__(self):
		return self.email


class Test(models.Model):
	name = models.CharField(max_length=24)
	address = models.CharField(max_length=45)

	def __str__(self):
		return self.name
