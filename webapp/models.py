from django.db import models

# Create your models here.
class employees(models.Model):
    firstname=models.CharField(max_length=10, default="noname")
    lastname=models.CharField(max_length=10,default="noname")
    # emp_id= models.IntegerField()

    def __str__(self):
        return self.firstname