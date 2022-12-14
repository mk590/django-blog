from django.forms import ModelForm
from .models import Blog


#  to bind the author and the username

class BlogForm(ModelForm):
    class Meta:
     model=Blog
     fields=['title','tags','description','content','image_attached']
