from django.shortcuts import render
# from basicapp import forms
from django.urls import reverse
from basicapp.forms import UserForm,UserProfileInfoForm
# Create your views here.
# from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate, login, logout
def index(request):
    return render(request,'basicapp/index.html')
@login_required
def special(request):
    return HttpResponse('You are successfully loged in')
@login_required #directly above function so the below function work in login is done only
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))
def register(request):

    registered=False

    if request.method=='POST':

        #  assigning one variable to take values from the forms
        user_form=UserForm(data=request.POST)
        profile_form=UserProfileInfoForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():

            user=user_form.save()
            # for to go in settings to user password hashing
            user.set_password(user.password)
            user.save()
            #This is main where profile variable is taking data from both and saving it in database, where we used one attribute in UserProfileInfoForm user to add the additional
            # form details to default user buitin from django, to save the details from user form to user model profile.user to assign to attributes of user database
            profile=profile_form.save(commit=False)
            profile.user=user
            if 'profile_pic' in request.FILES:
                profile.profile_pic=request.FIles['profile_pic']
            profile.save()
            registered=True
        else:
            print(user_form.errors,profile_form.errors)
    else:
        user_form=UserForm()
        profile_form=UserProfileInfoForm()
    return render(request,'basicapp/registration.html',{'user_form':user_form,'profile_form':profile_form,'registered':registered})

def user_login(request):

    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')

        user=authenticate(username=username,password=password)
        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse("Account is Not active :(")
        else:
            print("Some one tried to login")
            print("Username :{} and Password :{}".format(username,password))
            return HttpResponse("Invalid login details supplied")
    else:
        return render(request,'basicapp/login.html')
