from rest_framework import serializers

# TODO: опишите необходимые сериализаторы

from .models import Sensor, Measurement

# class SensorSerializers(serializers.Serializer):
#     id = serializers.IntegerField()
#     name = serializers.CharField()


class SensorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sensor
        fields = ['id', 'sensor_name', 'description']


class MeasurementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Measurement
        fields = ['sensor', 'temperature', 'created_at', 'image']


class SensorDetailSerializer(serializers.ModelSerializer):
    measurements = MeasurementSerializer(source='sensor', read_only=True, many=True)

    class Meta:
        model = Sensor
        fields = ['id', 'sensor_name', 'description', 'measurements']