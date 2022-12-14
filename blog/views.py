from django.shortcuts import render,redirect
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
  
  
# how this update of blog works eachline explanation   
def specific_blog_update(request,pk):
        if request.method == "POST":
            particularBlog = Blog.objects.get(pk= pk)
            update = BlogForm(request.POST, request.FILES ,instance = particularBlog)
            if update.is_valid():
                update.save()
                return redirect('home')
            
        particularBlog = Blog.objects.get(pk= pk)
        content = BlogForm(instance=particularBlog)
        info = {'data':content}
        return render(request,"update.html",info)
    
    
def specific_blog_del(request,pk):
        particular_blog=Blog.objects.get(pk=pk)
        particular_blog.delete()
        return redirect('home')
    
# what is pk=pk here , is it similar to id=passed parameter 
# also it has a issue that in the django the ids/count is not updated  
