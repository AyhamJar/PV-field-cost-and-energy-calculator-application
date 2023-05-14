from django.contrib import admin
from django.urls import path
from PVapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('mono/', views.mono),
    path('poly/', views.poly),
    path('thin/', views.thin),
    path('calculate/', views.calculate),
]
