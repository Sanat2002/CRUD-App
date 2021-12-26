from rest_framework import serializers
from crudapp.models import users

class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = users
        fields = "__all__"