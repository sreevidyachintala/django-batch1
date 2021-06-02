from django.db import models

# Create your models here.

class Register(models.Model):

	name= models.CharField(max_length=30)

	email = models.EmailField(max_length=30)

	age = models.IntegerField()

	mobile_no = models.CharField(max_length=10)

	