from django.urls import path
from .import views

urlpatterns = [
    path('',views.index,name='home page'),
    path('page2',views.page2,name='second page')
]