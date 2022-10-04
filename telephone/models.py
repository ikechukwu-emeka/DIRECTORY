from django.db import models

# Create your models here.
class Telephone(models.Model):
    forename=models.CharField(max_length=20)
    surname=models.CharField(max_length=20)
    middle_name=models.CharField(max_length=20,null=True)
    phone_number=models.CharField(max_length=11)
    gender=models.CharField(max_length=6)

    def __str__(self):
        return self.first_name