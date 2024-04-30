from rest_framework import serializers

# import model from models.py
from .models import StudentModel, EmployeeModel,CarModel

class StudentSerializer(serializers.ModelSerializer):
	class Meta:
		model = StudentModel
		fields = ('id','name', 'email','city')
class EmployeeSerializer(serializers.ModelSerializer):
	
	class Meta:
		model = EmployeeModel
		fields = ('id','emp_name', 'emp_email','emp_city')
class CarSerializer(serializers.ModelSerializer):
	class Meta:
		model = CarModel
		fields = ('id','car_name', 'car_model','year')