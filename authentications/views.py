from django.shortcuts import render, redirect
from django.conf import settings
from django.contrib import messages
from django.contrib.auth import get_user_model, authenticate, login, logout

User = get_user_model()

def signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        fullname = request.POST.get('fullname')
        phone = request.POST.get('phone')
        image = request.FILES.get('image')
        is_doctor = request.POST.get('is_doctor')== 'on'

        user_model = User.objects

        if password != confirm_password:
            messages.info(request, 'Password not match')
            return redirect('authentications:signup')
        elif User.objects.filter(username=username).exists():
            messages.info(request, f'{username} already exists')
            return redirect('authentications:signup')
        else:
            user_data = User.objects.create_user(username=username, 
                email=email, password=password,
                fullname=fullname, phone = phone, image=image, is_doctor=is_doctor)
            messages.info(request, 'Signed up successfully')
            return redirect('authentications:login_view')

    return render(request, 'authentications/signup.html')


def login_view(request):
    user = request.user
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, 'Logged in successfully.')

            if user.is_doctor:
                return redirect('view_appointment')
            return redirect('index')
        else:
            messages.error(request, 'Invalid username or password.')

    return render(request, 'authentications/login.html')

def signout(request):
    # user = request.user
    logout(request)

    messages.error(request, 'You logged out. Login again?')
    return redirect('authentications:login_view')
