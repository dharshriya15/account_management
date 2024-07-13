from django.db import models
import uuid

def generate_token():
    return str(uuid.uuid4())

class Account(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True, null=True, blank=True)
    app_secret_token = models.CharField(max_length=100, default=generate_token) 

class Destination(models.Model):
    account = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='destinations')
    url = models.URLField()
    name = models.CharField(max_length=100)