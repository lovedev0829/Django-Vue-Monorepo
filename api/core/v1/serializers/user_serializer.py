from rest_framework import serializers
from api.models import User


class UserSerializer(serializers.ModelSerializer):
    
    class Meta:
        
        model = User
        fields = ["id", "email", "username", "first_name", "middle_name", "last_name"]
        unique_together = ("email", "username")