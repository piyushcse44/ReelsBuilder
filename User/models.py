from django.db import models
from User import const
import uuid
from django.contrib.auth.models import User

# Create your models here.

class Videos(models.Model):

    id = models.UUIDField(default=uuid.uuid4,editable=False,primary_key=True,unique=True)
    title = models.CharField(max_length=200,null=False,blank=False,default="Unknown")
    video_id = models.CharField(max_length=200,null=False,blank=False)
    download_link = models.URLField(max_length=200,unique=True,null=False,blank=False)
    time_created = models.DateTimeField()

    def __str__(self):
        return str(self.title)



class UserInfo(models.Model):

    id = models.UUIDField(default=uuid.uuid4,editable=False,primary_key=True,unique=True)
    user = models.OneToOneField(User,on_delete=models.CASCADE,null=True,blank=True)
    user_email = models.EmailField(max_length=200,null=False,blank=False)
    user_video = models.ManyToManyField(Videos,blank=True)
    subscription_status = models.CharField(max_length=100,choices=const.subscription_status_list)

    def __str__(self):
        return self.user_email



class GeneraterVideImage(models.Model):

    id = models.UUIDField(default=uuid.uuid4,editable=False,primary_key=True,unique=True)
    title = models.CharField(max_length = 200 ,null=False,blank=False,default ="My_Image")
    status = models.CharField(max_length=100,choices=const.list_generator_image_status)
    generater_video_image = models.ImageField(upload_to="images/",default="images/default.pdf")
    created_on = models.DateTimeField(auto_now_add=True)

    
    def __str__(self):
       return  self.title