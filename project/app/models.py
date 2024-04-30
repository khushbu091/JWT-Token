from django.db import models

# Create your models here.
class StudentModel(models.Model):
    name = models.CharField(max_length = 200)
    email = models.EmailField()
    city = models.CharField(max_length=100)
    def __str__(self):
        return self.name
class EmployeeModel(models.Model):
    emp_name = models.CharField(max_length = 200)
    emp_email = models.EmailField()
    emp_city = models.CharField(max_length=100)
    def __str__(self):
        return self.emp_name
class CarModel(models.Model):
    car_name = models.CharField(max_length = 200)
    car_model = models.CharField(max_length=200)
    year = models.CharField(max_length=100)
    def __str__(self):
        return self.car_name