from django.urls import path
from . import views as v

urlpatterns = [
    path('',v.home,name='home'),
    path('home',v.home,name='home'),
    path('sign-up',v.sign_up,name='sign_up'),
    path('create-post',v.create_post,name='create_post'),
]
