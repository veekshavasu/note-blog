from django.shortcuts import render, redirect
from .forms import UserForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
#from mail_templated import send_mail

def index(request):
    return render(request,'design.html')
@login_required
def special(request):
    return HttpResponse("You are logged in !")
@login_required
def user_Logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))
def register(request):
    registered = False
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        if user_form.is_valid(): 
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            registered = True
        else:
            print(user_form.errors)
    else:
        user_form = UserForm()
    return render(request,'registration.html',
                          {'user_form':user_form,
                           'registered':registered})
def user_Login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request,user)
                return redirect('/signin')
            else:
                return HttpResponse("Your account was inactive.")
        else:
            print("Someone tried to login and failed.")
            print("They used username: {} and password: {}".format(username,password))
            return HttpResponse("Invalid login details given")
    else:
        return render(request, 'login.html', {})

def signin(request):
    return redirect('/looks')

def looks(request):
    return render(request,'looks.html',{})


def admin1(request):
    return render(request,'admin1.html',{})

def feedback(request):
    return render(request,'feedback.html',{})






# def send_email(site_id, email):
#     subject = "Sub"
#     from_email, to = EMAIL_FROM, email
#     text_content = 'Text'
#     html_content = render_to_string(
#         'app/includes/email.html',
#         {'pk': site_id}
#     )
#     msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
#     msg.attach_alternative(html_content, "text/html")
#     msg.send()


# def send_mail(request):
#     return render(request,'email.html',{'user':user},from_email,[user,email]) 