from django.urls import path
from .import views

urlpatterns = [
    path('',views.index,name="index"),
    path('delete/<int:id>/',views.deletedata,name="del"),
    path('update/<int:id>/',views.updatedata,name="up")
]
