from django.urls import path

from . import views

urlpatterns = [
    path('',views.splash, name='splash'),
    path('home',views.home, name='home'),
    path('register',views.register, name='register'),
    path('login',views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('delete/<int:id>', views.delete, name='delete'),
    # path('distance', views.distance, name='distance'),
]