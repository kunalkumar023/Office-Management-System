from django.db import models

# Create your models here.


class employee(models.Model):
    firstname= models.CharField(max_length=50,null=False)
    lastname= models.CharField(max_length=50)
    salary = models.IntegerField(default="0")
    bonus = models.IntegerField(default="0")
    phone = models.IntegerField(default="0")
    hiredate = models.DateField()

    def __str__(self):
        return self.firstname