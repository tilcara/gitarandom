
from django.urls import path
from . import views

app_name = 'gitarandom'

urlpatterns = [
    
    path('', views.home ,name='home'),

]