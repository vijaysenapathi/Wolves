from django.db import models

# Create your models here.
class User(models.Model):
  name = models.CharField(max_length=500)
  number = models.CharField(max_length=10)
  def __str__(self):
    return self.name + ' [' + self.number + ']'