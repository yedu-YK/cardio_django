
from django.contrib import admin
from django.urls import path

from home import views

urlpatterns = [
    path('',views.welcome, name='welcome'),
    path('add',views.hform, name='adddata'),
    path('predict/(?P<pk>)/',views.predict_now, name='predict_now'),
]
