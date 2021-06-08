from django.db import models
from django.contrib.auth.models import User

EMPLOYEES_STRENGTH = (
    ('1','less than 10'),('2','20-100'),('3','100-1000'),('4','1000-5000'),('5','more than 5000'),
)


class Company(models.Model):
    companyname = models.CharField(max_length=256,null=False)
    address = models.CharField(max_length=256,null=True)
    companyemail= models.EmailField(max_length=254,null=True)
    dateofregistration = models.DateField(null=True)
    description = models.CharField(max_length=256,null=True)
    companyphonenumber = models.CharField(max_length=256,null=True)
    numberofemployees = models.CharField(
       max_length=32,
       choices=EMPLOYEES_STRENGTH,
       default='1000-5000',
   )

    def __str__(self):
        return self.companyname



class Companyuser(User):
    description = models.CharField(max_length=256,null=False)
    mobilenumber=models.CharField(max_length=256,null=False)    
    company = models.ForeignKey(Company, on_delete=models.CASCADE,blank=True, null=True)


    #manytomany 

# Create your models here.

class BenchResource(models.Model):    
    employedtocompany = models.ForeignKey(Company, on_delete=models.CASCADE,blank=True, null=True,related_name='employedto')
    contractedtocompany = models.ForeignKey(Company, on_delete=models.CASCADE,blank=True, null=True,related_name='contractedto')
    email=models.CharField(max_length=254,null=True)
    firstname = models.CharField(max_length=256,null=True)
    lastname = models.CharField(max_length=256,null=True)
    mobile = models.CharField(max_length=100,null=True)
    primaryskills = models.CharField(max_length=256,null=True)
    secondaryskills = models.CharField(max_length=256,null=True)
    ratecard = models.IntegerField(null=True)
    currentlocation = models.CharField(max_length=256,null=True)
    totalexperience = models.IntegerField(null=True)
    description = models.CharField(max_length=256,null=True)

    def __str__(self):
        return self.firstname+self.lastname



    #contracted to company
    # Employee of Company
    # email
    # many to many BenchResourceFeedback
    #Firstname
    #lastname
    #mobile
    #Promary Skills
    #secondary Skills
    #ratecard per month2
    #Resume file
    #Location
    #Total experience
    # Description 
    # Overall Rating

class Employee(models.Model):  
    eid = models.CharField(max_length=20)  
    ename = models.CharField(max_length=100)  
    econtact = models.CharField(max_length=15)  





