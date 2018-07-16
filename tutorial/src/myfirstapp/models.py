from django.db import models
# Create your models here.
from django.db import models
# from django.contrib.postgres.fields import JSONField

class FirstApp(models.Model):
    fname = models.CharField()
    lname = models.CharField()
    age = models.IntegerField(default=60)

    # def display(self):
    #     return self.fname + self.lname, self.age
