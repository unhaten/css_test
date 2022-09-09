from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('testroom', views.testroom, name='testroom'),
    path('task', views.task, name='task'),
]
