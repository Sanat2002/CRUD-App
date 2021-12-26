from django.urls import input,path
from django.urls.conf import include
from rest_framework.routers import DefaultRouter
import views

router = DefaultRouter()
router.register('api/',views.UserApi,basename="userapi")

urlpatterns = [
    path('',include(router.urls))
]
