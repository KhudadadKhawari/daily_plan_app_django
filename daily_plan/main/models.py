from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Archive(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField(null=True)
    category = models.CharField(max_length=100, null=True)
    date_created = models.DateField(auto_now_add=True)

    def __str__(self) -> str:
        return self.title

class EducationalNote(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField(null=True)
    date_created = models.DateField(auto_now_add=True)

    def __str__(self) -> str:
        return self.title

class PersonalNote(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField(null=True)
    date_created = models.DateField(auto_now_add=True)

    def __str__(self) -> str:
        return self.title

class BusinessNote(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField(null=True)
    date_created = models.DateField(auto_now_add=True)

    def __str__(self) -> str:
        return self.title

