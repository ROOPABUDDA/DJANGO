from rest_framework import serializers
from .models import FirstApp
from django.db import models


class First(serializers.ModelSerializer):
    fname = models.CharField()
    lname = models.CharField()
    age = models.IntegerField()

    model = FirstApp
    # object.save()


