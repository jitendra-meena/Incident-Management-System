from rest_framework import serializers
from .models import Incident
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['username', 'password']

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password']
        )
        return user
    
class IncidentSerializer(serializers.ModelSerializer):
    reporter_name = serializers.ReadOnlyField(source='reporter.username')

    class Meta:
        model = Incident
        fields = ['id', 'incident_id', 'reporter_name', 'incident_details', 'reported_datetime', 'priority', 'status']
