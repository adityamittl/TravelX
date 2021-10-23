from django.contrib import admin
from .models import *
# Register your models here.


admin.site.register(profile)
admin.site.register(friend_list)
admin.site.register(bill)
admin.site.register(sent_request)
admin.site.register(recieve_request)