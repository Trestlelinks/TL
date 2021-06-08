from django.shortcuts import render,redirect
from .forms import BenchresourceForm,EmployeeForm,UserRegisterForm,CompanyRegisterForm
from .models import BenchResource,Employee,Companyuser
from django.contrib.auth.forms import AuthenticationForm
from django.template.loader import get_template
from django.core.mail import EmailMultiAlternatives
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from .forms import UserRegisterForm
from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template
from django.template import Context

# Create your views here.

def benchresource_list(request):
    return render(request, 'company/bench_list.html')


def benchresource_form(request):
    form = BenchresourceForm()    
    return render(request, 'company/base.html')
   # return render(request, 'company/bench_form.html',{'form':form})

#def benchresource_delete(request):
  #  return 


def benchresource(request):
    if request.method == 'POST':
        print('in if')
        form = BenchresourceForm(request.POST)
        print('form details')
        #print(form)
        print(form.is_valid())
        print(form.errors)
        #print(form.mobile)
        if form.is_valid():
            print('form is valid')
            try:
                form.save()
                return redirect('company/benchshow')
            except Exception as e:
                logger.error('Failed to upload to ftp: '+ str(e))
                #pass
    else:
        form = BenchresourceForm()
    return render(request,'company/bench.html',{'form':form})

def benchshowview(request):
    benchresources = BenchResource.objects.all()
    return render(request,"company/benchshow.html",{'benchresources':benchresources})  

def benchedit(request, id):
    benchresource = BenchResource.objects.get(id=id)
    return render(request,'company/benchedit.html', {'benchresource':benchresource})  

def benchupdate(request, id):  
    benchresource = BenchResource.objects.get(id=id)  
    form = BenchresourceForm(request.POST, instance = benchresource)  
    if form.is_valid():  
        form.save()  
        return redirect("company/benchshow")  
    return render(request, 'company/benchedit.html', {'benchresource': benchresource})  
def benchdestroy(request, id):  
    benchresource = BenchResource.objects.get(id=id)  
    benchresource.delete()  
    return redirect("company/benchshow")  


def emp(request):  
    if request.method == "POST":  
        form = EmployeeForm(request.POST)  
        if form.is_valid():  
            try:  
                return redirect('/')  
            except:  
                pass  
    else:  
        form = EmployeeForm()  
    return render(request,'index.html',{'form':form})  



# Users 

def index(request):
    return render(request, 'company/index.html', {'title':'index'})


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            ######################### mail system ####################################
            htmly = get_template('company/Email.html')
            d = { 'username': username }
            subject, from_email, to = 'welcome', 'your_email@gmail.com', email
            html_content = htmly.render(d)
            msg = EmailMultiAlternatives(subject, html_content, from_email, [to])
            msg.attach_alternative(html_content, "text/html")
            msg.send()
            ##################################################################
            messages.success(request, f'Your account has been created ! You are now able to log in')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'company/register.html', {'form': form, 'title':'reqister here'})
  

def Login(request):
    if request.method == 'POST':

        # AuthenticationForm_can_also_be_used__

        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username = username, password = password)
        if user is not None:
            form = login(request, user)
            messages.success(request, f' wecome {username} !!')
            cu = Companyuser.objects.get(username=username)
            print(cu)
            print(user)
            if cu.company is not None:
                return('/company/')
            else:
                return('/companyregister/')
        else:
            messages.info(request, f'account done not exit plz sign in')
    form = AuthenticationForm()
    return render(request, 'company/login.html', {'form':form, 'title':'log in'})


    ### company register
   

def companyregister(request):
    if request.method == 'POST':
        form = CompanyRegisterForm(request.POST)
        if form.is_valid():
            form.save()               
            return redirect('company/benchshow')
    else:
        form = CompanyRegisterForm()
    return render(request, 'company/companyregister.html', {'form': form, 'title':'register your company'})