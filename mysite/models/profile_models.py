from django.db import models
from django.contrib.auth import get_user_model

class Profile(models.Model):
  user = models.OneToOneField(get_user_model(), primary_key=True, unique=True, on_delete=models.CASCADE)
  username = models.CharField(default="匿名ユーザ", max_length=30)
  zipcode = models.CharField(default="", max_length=8)
  prefecture = models.CharField(default="", max_length=6)
  city = models.CharField(default="", max_length=100)
  address = models.CharField(default="", max_length=200)