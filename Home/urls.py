from django.urls import path
from .views import Home,Login,Signup
urlpatterns = [
    path('home', Home.as_view()),
    path('Login',Login.as_view()),
    path('Signup',Signup.as_view()),

]
