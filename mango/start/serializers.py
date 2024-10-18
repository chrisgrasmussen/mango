from .models import Start
from rest_framework import serializers

class StartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Start
        fields = ('id', 'title', 'timestamp')