from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField
from django.utils.timezone import now

class blog(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200,null=True)
    catagory = models.CharField(max_length=100,null=True)
    thumbnail = models.ImageField(default="defthumb.jpg")
    content = models.TextField()
    date = models.DateTimeField(default=now)
    likes = models.IntegerField(default=0)

class comments(models.Model):
    blog = models.ForeignKey(blog,on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    comment = models.TextField()
    recomment = models.ForeignKey('self',on_delete=models.CASCADE, blank=True,null=True)