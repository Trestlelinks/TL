from django import forms
from .models import BenchResource,Employee,Companyuser,Company
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class BenchresourceForm(forms.ModelForm):    
    class Meta:
        model = BenchResource
        fields = ('__all__')



class EmployeeForm(forms.ModelForm):  
    class Meta:  
        model = Employee  
        fields = "__all__"  


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()    
    first_name = forms.CharField(max_length = 20)
    last_name = forms.CharField(max_length = 20)
    class Meta:
        model = Companyuser
        fields = ['first_name','last_name','username', 'email', 'mobilenumber', 'password1', 'password2']


class CompanyRegisterForm(forms.ModelForm):
    class Meta:
        model = Company
        fields= ['companyname','description','address','companyemail','dateofregistration','companyphonenumber','numberofemployees']

        