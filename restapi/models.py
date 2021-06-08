from django.db import models

# Create your models here.
class employees(models.Model):
    firstname=models.CharField(max_length=20)
    lastname=models.CharField(max_length=20)
    emp_id=models.IntegerField()


    def _str_(self):
        return self.firstname