from django.db import models

# Create your models here.
class Authentication_information(models.Model):
    access_token = models.CharField(max_length=100)
    refresh_token = models.CharField(max_length=100)
    expiration_date = models.IntegerField()
