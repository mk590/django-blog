from django.urls import path

from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('form-blog/',views.form,name='form'),
    path('blog-del/<int:pk>/',views.specific_blog_del,name='specific_blog_del'),
    path('blog-update/<int:pk>/',views.specific_blog_update,name='specific_blog_update'),
    path('blog-view/<int:pk>/',views.specific_blog_view,name='specific_blog_view'),
 
]

# how it works
# what is use of path 
# waht is name here 
# first represents a url and second shows a view realted to that url 
#  path('blog/<int:pk>/',views.specific_blog,name='specific_blog'), pk is like the params in the react where the /<int:pk> kpart shows that after the slash a integer will be there which we have to pass to the view along with the request 

# in urls its better to use the - instead of the underscores 