from rest_framework import serializers
from .models import *

class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = Login
        fields = "__all__"


class PasswordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Password
        fields = "__all__"