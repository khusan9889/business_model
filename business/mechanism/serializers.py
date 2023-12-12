from rest_framework import serializers
from .models import Mechanism

class MechanismSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mechanism
        fields = ('name', 'model_id')