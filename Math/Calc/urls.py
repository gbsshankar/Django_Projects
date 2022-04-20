from django.urls import path
from . import views

urlpatterns = [    
    path('sum',views.sum,name='sum'),     
    path('email',views.email,name='email'),
]