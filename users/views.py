from django.shortcuts import render, redirect,HttpResponse
from django.contrib import messages
from .forms import UserRegisterForm

# for authorization 
from django.contrib.auth.decorators import login_required

def register(request):
    if request.method=='POST':
        user_form=UserRegisterForm(request.POST)
        if user_form.is_valid():
            user_form.save()
            
            username = user_form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            # these two lines are doing nothing the 
            
            return redirect('home')
        else:
            return HttpResponse("error")
    else:
        form = UserRegisterForm()
        return render(request, 'register.html', {'data': form})
    
    
@login_required
def profile(request):
    return render(request,'profile.html')