from django.contrib import admin
from django.urls import path,re_path
from .import views

urlpatterns = [
   path('user/<str:token>',views.user,name="user_object"),
   path('token/<str:code>',views.token,name="token_object") 

]