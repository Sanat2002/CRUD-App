from crudapp.models import users
from .serializers import UserSerializers
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.authentication import BasicAuthentication, SessionAuthentication

class UserApi(viewsets.ModelViewSet):
    queryset = users.objects.all()
    serializer_class = UserSerializers
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]