from django.urls import path
from .import views

urlpatterns = [
    path('login/',views.login1,name='login page'),
    path('register/',views.register,name='register page'),
    path('login/Signup/',views.signup,name='sign in user'),
    path('logout',views.logout,name='logout page')
]