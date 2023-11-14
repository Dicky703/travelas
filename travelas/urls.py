from django.urls import path
from django.conf.urls import url
from . import views

app_name = 'travelas'


urlpatterns = [
path('index/', views.index, name = 'index'),
#path('about/', views.about, name = 'about'),
path('travelas/car/<car_name_url>/',views.car, name = 'car'),
#url(r'^car/(?P<car_name_url>\w+)/$', views.car, name='car'),
path('travelas/add_car/', views.add_car, name = 'add_car'),
path('travelas/register/', views.register, name = 'register'),
path('travelas/login/', views.user_login, name = 'login'),
path('travelas/logout/', views.user_logout, name = 'logout'),
path('travelas/restricted/', views.restricted, name = 'restricted'),
path('<id>/delete/', views.delete_view, name = 'delete'),
path('<id>', views.detail_view, name = 'details' ),
path('update/<id>/', views.update_view, name = 'update'),
]
