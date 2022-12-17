from django.shortcuts import render,redirect,HttpResponse
from .models import *
from .forms import *


# for authorization 
from django.contrib.auth.decorators import login_required

def home(request):
    all_blog=Blog.objects.all()
    
    return render(request,'home.html',{'data':all_blog})


@login_required      
def form(request):
    if request.method=="POST":
        form=BlogForm(request.POST,request.FILES)
        if form.is_valid:
            blog=form.save(commit=False)
            blog.author=request.user
            blog.save()

            return redirect('home')
        
    else:
        form=BlogForm()
        return render(request,'form.html',{'data':form})


def specific_blog_view(request,pk):
        particular_blog=Blog.objects.get(pk=pk)
        
        return render(request,'view_blog.html',{'data':particular_blog})
  
def specific_blog_update(request,pk):
        if request.method == "POST":
            particularBlog = Blog.objects.get(pk= pk)
            updated_blog = BlogForm(request.POST, request.FILES ,instance = particularBlog)
            if updated_blog.is_valid():
                updated_blog.save()
                return redirect('home')
            
        particularBlog = Blog.objects.get(pk= pk)
        content = BlogForm(instance=particularBlog)
        info = {'data':content}
        return render(request,"update.html",info)
    
    
def specific_blog_del(request,pk):
        particular_blog=Blog.objects.get(pk=pk)
        particular_blog.soft_delete()
        return redirect('home')



from django.contrib import messages
from .forms import UserRegisterForm

# for authorization 
from django.contrib.auth.decorators import login_required

def register(request):
    if request.method=='POST':
        user_form=UserRegisterForm(request.POST)
        if user_form.is_valid():
            user_form.save()          
            return redirect('home')
        else:
            return HttpResponse("error")
    else:
        form = UserRegisterForm()
        return render(request, 'register.html', {'data': form})
    
    
@login_required
def profile(request):
    return render(request,'profile.html')