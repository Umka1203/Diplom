from rest_framework.serializers import ModelSerializer
from django.contrib.auth.models import User
from .models import Profile

class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

# class IsUserSerializer(ModelSerializer):
#     class Meta:
#         model = User
#         fields = '__all__'