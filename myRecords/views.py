from django.shortcuts import render
from rest_framework import viewsets
from .models import ChickenRecord, CowRecord, HorticultureRecord
from .serializers import ChickenRecordSerializer, CowRecordSerializer, HorticultureRecordSerializer

# Create your views here.
class ChickenRecordViewSet(viewsets.ModelViewSet):
    queryset = ChickenRecord.objects.all().order_by('-date')
    serializer_class = ChickenRecordSerializer

class CowRecordViewSet(viewsets.ModelViewSet):
    queryset = CowRecord.objects.all().order_by('-date')
    serializer_class = CowRecordSerializer
# Compare this snippet from records/myRecords/urls.py:

class HorticultureRecordViewSet(viewsets.ModelViewSet):
    queryset = HorticultureRecord.objects.all().order_by('-planting_date')
    serializer_class = HorticultureRecordSerializer
# Compare this snippet from records/myRecords/serializers.py:
