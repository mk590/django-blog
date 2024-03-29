from django.db import models
from django.contrib.auth.models import User

from django.utils.timezone import now
class SoftDeleteManager(models.Manager):

    def get_queryset(self):
        return super().get_queryset().filter(deleted_at__isnull=True)
    
class SoftDelete(models.Model):

    deleted_at = models.DateTimeField(null=True, default=None)
    objects = SoftDeleteManager()
    all_objects = models.Manager()

    def soft_delete(self):
        self.deleted_at = now()
        self.save()

    def restore(self):
        self.deleted_at = None
        self.save()

    class Meta:
        abstract = True

class Tags(models.Model):
    category=models.CharField(max_length=100)
    def __str__(self):
        return self.category
    
class Blog(SoftDelete):
    title=models.CharField(max_length=200)
    tags=models.ManyToManyField(Tags)
    description=models.CharField(max_length=500)
    content=models.CharField(max_length=1000)
    author=models.ForeignKey(User,on_delete=models.CASCADE)
    date_created=models.DateTimeField(auto_now_add=True)
    image_attached= models.ImageField(null=True ,blank=True, upload_to="images/")
    
    class Meta:
        ordering=['date_created']
