from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',default,name = 'Homepage'),
    path('users',all_users),
    path('pendingpayments',pendingPayment,name='pendingPayment'),
    path('paythebills/<slug:slug>',paybills),
    path('split',split),
    path('recieved',recieved_requests),
    path('acceptfriend/<slug:slug>',accept_friend),
    path('travel',travel),
    path('addfriend/<slug:slug>',add_friend),
    path('findfriends',findfriend),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)