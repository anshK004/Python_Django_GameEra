from django.db import models

# Create your models here.
from django.db import models

class Admin(models.Model):
    id = models.CharField(max_length=100, primary_key=True)
    password = models.CharField(max_length=100)
    fullname = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    contact = models.IntegerField(max_length=100)
    gender = models.CharField(max_length=100)
    date_of_birth = models.DateTimeField(max_length=100)
    address = models.CharField(max_length=100)
    registration_number = models.CharField(max_length=100)
    organisation_name = models.CharField(max_length=100)

class Customer(models.Model):
    id = models.CharField(max_length=100, primary_key=True)
    password = models.CharField(max_length=100)
    fullname = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    date_of_birth = models.DateTimeField(max_length=100)
    gender = models.CharField(max_length=100)
    contact = models.IntegerField(max_length=100)
    city = models.CharField(max_length=100)

class Employee(models.Model):
    id = models.CharField(max_length=100, primary_key=True)
    password = models.CharField(max_length=100)
    fullname = models.CharField(max_length=100)
    post = models.CharField(max_length=100)
    salary = models.IntegerField(max_length=100)
    date_of_birth = models.DateTimeField(max_length=100)
    contact = models.IntegerField(max_length=100)
    gender = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=100)

class Booking(models.Model):
    user_id = models.CharField(max_length=100, primary_key=True)
    booking_id = models.CharField(max_length=100)
    date_of_booking = models.DateTimeField(max_length=100)
    date_for_booking = models.DateTimeField(max_length=100)
    amount = models.IntegerField(max_length=100)
    status = models.CharField(max_length=100)

class Complaint(models.Model):
    complaint_id = models.CharField(max_length=100, primary_key=True)
    fullname = models.CharField(max_length=100)
    complaint = models.CharField(max_length=100)
    complaint_date = models.DateTimeField(max_length=100)
    contact = models.IntegerField(max_length=100)
    complaint_status = models.CharField(max_length=100)

class gamezonedetails(models.Model):
    registration_number = models.CharField(max_length=100, primary_key=True)
    place_name = models.CharField(max_length=100)
    details = models.CharField(max_length=100)
    contact = models.IntegerField(max_length=100)
    services = models.CharField(max_length=100)
    charges  = models.IntegerField(max_length=100)
    address = models.CharField(max_length=100)