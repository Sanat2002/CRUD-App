from django.db import models

# Create your models here.
class users(models.Model):
    name = models.CharField(max_length=50)
    email= models.EmailField()
    password = models.CharField(max_length=20)
    phone_no = models.CharField(max_length=15)

    def __str__(self):
        return self.name