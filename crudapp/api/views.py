from crudapp.models import users
from .serializers import UserSerializers
from rest_framework import viewsets

class UserApi(viewsets.ModelViewSet):
    queryset = users.objects.all()
    serializer_class = UserSerializers