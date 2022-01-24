import imp
from pyexpat import model
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Plan(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField(null=True)
    status = models.IntegerField(default=0)
    date_created = models.DateField(auto_now_add=True)

    def __str__(self) -> str:
        return self.description