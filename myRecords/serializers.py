from rest_framework import serializers
from .models import ChickenRecord, CowRecord, HorticultureRecord

class CowRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = CowRecord
        fields = ['date', 'cows', 'milk', 'feed', 'notes']

class ChickenRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChickenRecord
        fields = ['date', 'hens', 'eggs', 'feed', 'notes']

class HorticultureRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = HorticultureRecord
        fields = ['crop_name', 'crop_type', 'planting_date', 'harvest_date', 'quantity_harvested', 'unit', 'notes']
        