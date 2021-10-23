from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now
# Create your models here.


class profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=60)
    mobile = models.CharField(max_length=15)
    email = models.EmailField()
    image = models.ImageField(upload_to="profile_pictures",default="profile_pictures/profile.jpg")

    def __str__(self):
        return str(self.user)

class friend_list(models.Model):
    user = models.OneToOneField(User,related_name='user_name',on_delete=models.CASCADE)
    friend_count = models.IntegerField(default= 0)
    friends = models.ManyToManyField(User,null=True,blank=True)
    

class bill(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    creator = models.CharField(max_length=100)
    ammount = models.FloatField()
    time = models.DateTimeField(default=now)
    paid = models.BooleanField(default=False)
    bill_image = models.CharField(max_length=150,blank = True,null = True)

class sent_request(models.Model):
    from_user = models.ForeignKey(User, related_name='sent_from', on_delete=models.CASCADE)
    to_user = models.ForeignKey(User,related_name='sent_to', on_delete=models.CASCADE)
    is_accepted = models.BooleanField(default=False)

class recieve_request(models.Model):
    from_user = models.ForeignKey(User, related_name='recieve_from', on_delete=models.CASCADE)
    to_user = models.ForeignKey(User,related_name='recieved_to', on_delete=models.CASCADE)  
    accepted = models.BooleanField(default=False)
