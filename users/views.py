from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.forms import UserCreationForm
# Create your views here.

def logout_view(request):
    #log user out
    logout(request)
    return HttpResponseRedirect(reverse('learning_logs:index'))
def register(request):
    #register new user
    if request.method != 'POST':
        #Disaplay blank register form
        form=UserCreationForm()
    else:
        #process completed form
        form=UserCreationForm(data=request.POST)

        if form.is_valid():
            new_user=form.save()
            #log the user and redirect to home page
            authenticated_user=authenticate(username=new_user.username,password=request.POST['password1'])
            login(request,authenticated_user)
            return HttpResponseRedirect(reverse('learning_logs:index'))

    context={'form':form}
    return render(request,'users/register.html',context)
