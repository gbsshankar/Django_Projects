from django.urls import path
from . import views

urlpatterns=[ path('',views.Login,name='Login'),
             path('Login',views.Login,name='Login'),
             path('Holemaking',views.Holemaking,name='Holemaking'),
             path('Milling',views.Milling,name='Milling'),
             path('Turning',views.Turning,name='Turning'),
             path('Systems',views.Systems,name='Systems'),
             path('SCEndmill',views.SCEndmill,name='SCEndmill'),
             path('SCdrill',views.SCdrill,name='SCdrill')] 