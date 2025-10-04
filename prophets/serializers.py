from rest_framework import serializers
from prophets.models import Prophet

class ProphetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prophet
        fields = '__all__'