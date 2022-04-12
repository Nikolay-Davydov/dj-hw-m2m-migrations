# TODO: опишите необходимые обработчики, рекомендуется использовать generics APIView классы:
# TODO: ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView

from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView, RetrieveAPIView
from .models import Sensor, Measurement
from .serializers import SensorSerializer, MeasurementSerializer
from rest_framework.response import Response
from rest_framework.generics import ListAPIView

from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.views import APIView


class SensorView(ListAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer


class CreateSensorView(ListCreateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer

    def create_sensor(self, request):
        sensor_name = request.POST.get('sensor_name')
        description = request.POST.get('description')
        Sensor(sensor_name=sensor_name, description=description).save()
        return Response({'status': 'Датчик создан'})


class ChangeSensorView(RetrieveUpdateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer


class CreateMeasurementView(CreateAPIView):
    queryset = Measurement.objects.all
    serializer_class = MeasurementSerializer

    def create_measurement(self, request):
        sensor = request.POST.get('sensor')
        temperature = request.POST.get('temperature')
        image = request.POST.get('image')
        MeasurementSerializer(sensor=sensor, temperature=temperature, image=image).save()
        return Response({'status': 'Измерение выполнено'})


class SensorDetailsView(RetrieveAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer
