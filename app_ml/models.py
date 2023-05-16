"""from django.db import models

class Cardio(models.Model):
    id = models.AutoField(primary_key=True)
    gender = models.IntegerField(choices=((1, 'Female'), (2, 'Male')))
    height = models.FloatField()
    weight = models.FloatField()
    systolic_pressure = models.IntegerField()
    diastolic_pressure = models.IntegerField()
    cholesterol = models.IntegerField(choices=((1, 'Normal'), (2, 'Above normal'), (3, 'Well above normal')))
    glucose = models.IntegerField(choices=((1, 'Normal'), (2, 'Above normal'), (3, 'Well above normal')))
    smoker = models.BooleanField()
    alcohol_intake = models.BooleanField()
    physical_activity = models.BooleanField()"""


from django.db import models

# Create your models here.
class Patient(models.Model):
    name = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    age = models.FloatField()
    gender = models.FloatField()
    weight = models.FloatField()
    height = models.FloatField()
    diastolic_pressure = models.FloatField()
    systolic_pressure = models.FloatField()
    cholesterol = models.FloatField()
    glucose = models.FloatField()
    smoker = models.BooleanField()
    alcohol_intake = models.BooleanField()
    physical_activity = models.BooleanField()
