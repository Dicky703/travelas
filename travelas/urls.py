from django.urls import path
from django.conf.urls import url
from . import views



urlpatterns = [
path('index/', views.index, name = 'index'),
#path('about/', views.about, name = 'about'),
path('travelas/car/<car_name_url>/',views.car, name = 'car'),
#url(r'^car/(?P<car_name_url>\w+)/$', views.car, name='car'),
path('travelas/add_car/', views.add_car, name = 'add_car'),
path('travelas/register/', views.register, name = 'register'),
]