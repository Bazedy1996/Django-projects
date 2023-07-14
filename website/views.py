from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib  import messages
from .forms import SignupForm,AddRecordForm
from django.views.decorators.csrf import csrf_protect
from .models import Record

def home(request):
    records = Record.objects.all()
    return render(request,'home.html',{'records':records})


def login_user(request):
    
    if request.user.is_authenticated:
        return redirect('website:home')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request,username = username,password = password)
            if user is not None:
                login(request,user)
                return redirect('website:home')
            else:
                messages.error(request,'Invalid Username or Password')
    
    return render(request,'login.html')


def logout_user(request):

    logout(request)
    return redirect('website:login')

@csrf_protect
def register_user(request):

    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('website:login')
    else:
        form = SignupForm()
    return render(request,'register.html',{'form':form})
    

def customer_record(request,pk):

    customer_record = Record.objects.get(id=pk)
    return render(request,'record.html',{'customer_record':customer_record})


def delete_record(request,pk):

    customer_record = Record.objects.get(id=pk)
    customer_record.delete()
    return redirect('website:home')


def add_record(request):


    form = AddRecordForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('website:home')
    return render(request,'add_record.html',{'form':form})


def update_record(request,pk):

    current_record = Record.objects.get(id = pk)
    form = AddRecordForm(request.POST or None,instance=current_record)
    
    if form.is_valid():
        form.save()
        return redirect('website:home')
    return render(request,'update_record.html',{'form':form})


        

   
        




