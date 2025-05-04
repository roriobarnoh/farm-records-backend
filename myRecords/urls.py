from .views import ChickenRecordViewSet, CowRecordViewSet, HorticultureRecordViewSet
from django.urls import path, include
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'chicken-records', ChickenRecordViewSet, basename='chickenrecord')
router.register(r'cow-records', CowRecordViewSet, basename='cowrecord')
router.register(r'horticulture-records', HorticultureRecordViewSet, basename='horticulturerecord')


urlpatterns = [
    path('', include(router.urls)),
]