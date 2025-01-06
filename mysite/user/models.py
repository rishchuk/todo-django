from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class ToDo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.BooleanField(default=False)
    name = models.CharField(max_length=100)
    end_date = models.DateField(null=True, blank=True)