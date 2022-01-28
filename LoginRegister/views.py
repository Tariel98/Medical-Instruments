from django.shortcuts import render

# Create your views here.


def SignIn(request):
    return render(request, 'account/login.html')


def SignUp(request):
    return render(request, 'account/signup.html')


def ForgotPass(request):
    return render(request, 'account/password_reset.html')