from django.db import models
from django.db.models.fields.files import ImageField
from django.contrib.auth.models import User
import datetime
import os
# Create your models here.
def filepath(request,filename):
    old_file_name = filename
    timenow= datetime.datetime.now().strftime('%Y%m%H%M%S')
    filename = "%s%s" ,(timenow,old_file_name)
    return os.path.join('uploads/',str(filename))



class Post(models.Model):
    
    name = models.CharField(max_length=50)
    report_description = models.TextField(max_length=400,)

    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    post_time = models.DateTimeField(auto_now_add=True)

    section_name = models.CharField(max_length=50,blank=True, null=True)
    post_image = ImageField(upload_to=filepath,blank=True, null=True)
    post_description = models.TextField(max_length=400,blank=True, null=True)

    section_name1 = models.CharField(max_length=50,blank=True, null=True)
    post_image1 = ImageField(upload_to=filepath,blank=True, null=True)
    post_description1 = models.TextField(max_length=400,blank=True, null=True)

    section_name2 = models.CharField(max_length=50,blank=True, null=True)
    post_image2 = ImageField(upload_to=filepath,blank=True, null=True)
    post_description2 = models.TextField(max_length=400,blank=True, null=True)

    def __str__(self) -> str:
        return self.name