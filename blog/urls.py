from django.urls import path

from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('form_blog/',views.form,name='form'),
    path('blog_del/<int:pk>/',views.specific_blog_del,name='specific_blog_del'),
    path('blog_update/<int:pk>/',views.specific_blog_update,name='specific_blog_update'),
    path('blog_view/<int:pk>/',views.specific_blog_view,name='specific_blog_view'),
 
]

