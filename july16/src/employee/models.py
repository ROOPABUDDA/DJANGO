from django.db import models


# Create your models here.
class Employee(models.Model):
    code = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)

class Manager(models.Model):
    manager_code = models.IntegerField(primary_key=True)
    manager_name = models.CharField(max_length=50)
