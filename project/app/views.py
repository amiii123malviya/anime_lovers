from django.shortcuts import render
from .models import Student

# Create your views here.
def home(request):
    return render(request,'home.html')
def about(request):
    return render(request,'about.html')

def register(request):
    return render(request,'register.html')
def contact(request):
    return render(request,'contact.html')
def login(request):
    return render(request,'login.html')
def registerdata(request):
     print(request.method)
     print(request.POST)
     name=request.POST.get('name')
     email=request.POST.get('email')
     password=request.POST.get('password')
     Cpassword=request.POST.get('Cpassword')
     data=Student.objects.filter(Email=email)
     print(data)
     if data:
        msg='Already Email Exist'
        return render(request,'register.html',{'key':msg})
     else:
        if password==Cpassword:
            Student.objects.create(Name=name,
                               Email=email,
                               Password=password)
            msg="Register successfully"
            return render(request,'login.html',{'key':msg})
        
        else:
            msg="password and confirm password not matched"
            return render(request,'register.html',{'key':msg})
