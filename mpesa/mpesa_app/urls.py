from django.urls import path

from . import views


urlpatterns=[
    path('', views.home, name='home'),

    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('logout', views.logout, name='logout'),
    path('deposit', views.deposit, name='deposit'),
    #path('lipa_na_mpesa', views.lipa_na_mpesa, name='lipa_na_mpesa')
]