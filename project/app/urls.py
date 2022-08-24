from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('index/login', views.login, name="login"),
    path('index/addbook', views.addsubject, name="addbook"),
    path('index/addbook/subject/chapter', views.addchapter, name="chapter"),
    path('index/addbook/chapter/subchapter', views.subchapter, name="subchapter"),
    path('index/logout', views.logout, name='logout'),

]
