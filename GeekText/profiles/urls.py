from django.contrib import auth
from django.urls import path
from profiles import views
    


urlpatterns = [    
    path('register', views.register, name = "register"),
    path('postregister', views.postregister, name = "postregister"),
    path('login', views.signin, name = "login"),
    path('postsign', views.postsign),
    path('logout', views.logout, name = "logout"),
]