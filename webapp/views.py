from django.shortcuts import redirect, render
from .forms import CreateUserForm,LoginForm, CreateRecordForm, UpdateRecordForm
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from .models import Record
from django.contrib import messages
# Create your views here.

def home(request):

 return render(request, 'index.html')


#Register a User

def register(request):
  
    form = CreateUserForm()
    
    if request.method == "POST":
       form = CreateUserForm(request.POST)

       if form.is_valid():
          form.save()

          messages.success(request ,"Account Created Successfully!")

          return redirect('login')

    context = {'form': form}

    return render(request, 'register.html', context=context)

# Login a user

def Login(request):
   
   form = LoginForm()

   if request.method  == "POST":
      
       form = LoginForm(request, data = request.POST)

       if form.is_valid():
          
          username = request.POST['username']
          password = request.POST['password']

          user = authenticate(username=username, password=password)

          if user is not None:
               login(request, user)

               return redirect('dashboard')

     

   context = {'form': form}

   return render(request, 'my-login.html', context = context)

#- Dashboard



@login_required(login_url = 'login')
def dashboard(request):
     records = Record.objects.all()

     ctx = {'records': records}
     return render(request, 'dashboard.html', ctx)


def Logout(request):
    logout(request)


    return redirect('login')


@login_required(login_url='login')
def create_record(request):
    form = CreateRecordForm()

    if request.method == 'POST':
         form = CreateRecordForm(request.POST)

         if form.is_valid():
           
              
             form.save()

             messages.success(request, "Recorded created successfully.")

             return redirect('dashboard')
         
    context = {'form': form}

    return render(request, 'create-record.html', context) 



@login_required(login_url='login')
def update_record(request, pk):
     
     record = Record.objects.get(id = pk)

     form = UpdateRecordForm(instance=record)

     if request.method == 'POST':
         form = UpdateRecordForm(request.POST, instance= record)

         if form.is_valid():
             form.save()

             messages.success(request, "Record updated successfully.")

             return redirect('dashboard')
         
     context = {'form': form,
                'record': record}

     return render(request, 'update-record.html', context)  


@login_required(login_url='login')
def singular_record(request, pk):
     
     all_records = Record.objects.get(id = pk)

     context = {'record': all_records}
     return render(request, 'view-record.html', context=context)


@login_required(login_url='login')
def delete_record(request, pk):

    record = Record.objects.get(id = pk)



    record.delete()

    messages.success(request, "Record deleted successfully.")

    return redirect('dashboard')     