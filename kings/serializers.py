from rest_framework import serializers
from kings.models import King

class KingSerializer(serializers.ModelSerializer):
    class Meta:
        model = King
        fields = ["id", "name", "reign_start", "reign_end", "years_reigned", "is_good"]
