
from django.urls import path
from . import views

app_name = 'gitarandom'

urlpatterns = [
    
    path('', views.home ,name='home'),
    path('random_verse', views.random_verse ,name='random_verse'),

]