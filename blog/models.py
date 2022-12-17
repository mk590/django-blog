from django.db import models
from django.contrib.auth.models import User



class Tags(models.Model):
    category=models.CharField(max_length=100)
    def __str__(self):
        return self.category
    
class Blog(models.Model):
    title=models.CharField(max_length=200)
    tags=models.ManyToManyField(Tags)
    description=models.CharField(max_length=500)
    content=models.CharField(max_length=1000)
    author=models.ForeignKey(User,on_delete=models.CASCADE)
    date_created=models.DateTimeField(auto_now_add=True)
    image_attached= models.ImageField(null=True ,blank=True, upload_to="images/")
    
    class Meta:
        ordering=['date_created']
