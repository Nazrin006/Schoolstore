from django.contrib import messages, auth
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.shortcuts import render, redirect




def home(request):
    return render(request, 'home.html')

def register_view(request):
    # your registration logic here
    return render(request, 'register.html')


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('newpage')
        else:
            # Add an error message to be displayed in the template
            error_message = 'Invalid username or password.'
    else:
        error_message = ''

    context = {
        'error_message': error_message
    }
    return render(request, 'login.html', context)

def register(request):
    # if request.method == 'POST':
    #     username = request.POST['username']
    #     first_name = request.POST['first_name']
    #     last_name = request.POST['last_name']
    #     email = request.POST['email']
    #     password = request.POST['password']
    #     cpassword = request.POST['password1']
    #     if password == cpassword:
    #         if User.objects.filter(username=username).exists():
    #             messages.info(request,"username Taken")
    #             return redirect('register')
    #         elif User.objects.filter(email=email).exists():
    #             messages.info(request,"email taken")
    #             return redirect('register')
    #         else:
    #             user = User.objects.create_user(username=username, first_name=first_name, last_name=last_name,
    #                                             email=email, password=password)
    #             user.save();
    #             return redirect('login')
    #     else:
    #         messages.info(request, "Password not matching")
    #         return redirect('register')
    #     return redirect('/')
    return render(request, "register.html")

def new_page(request):
    return render(request, 'newpage.html')

def form_page(request):
   if request.method == 'POST':

            messages.success(request, 'Order confirmed!')
            return redirect('form_page')
   else:
     return render(request,'form.html')


def logout(request):
    logout(request)
    return redirect('home')
