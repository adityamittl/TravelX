from django.urls import path
from .views import *

urlpatterns = [
    path('blog/<slug:slug>', blogs),
    path('new-blog', new_blog),
    path('blog', all_blogs),
    path('like', like),
    path('myblogs', my_blogs),
    path('user/<slug:slug>', user_blog)
]