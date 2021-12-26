from django.urls import path
from django.urls.conf import include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register('userapi',views.UserApi,basename="userapi")

urlpatterns = [
    path('',include(router.urls)),
    path('auth/',include('rest_framework.urls'))
]
