from django.urls import path

from .views import ChangeSensorView, CreateSensorView, CreateMeasurementView, SensorDetailsView, SensorView


urlpatterns = [
    path('sensor/', SensorView.as_view()),
    path('sensor/create/', CreateSensorView.as_view()),
    path('sensor/change/<pk>/', ChangeSensorView.as_view()),
    path('measurements/', CreateMeasurementView.as_view()),
    path('sensor/details/<pk>/', SensorDetailsView.as_view())
    # TODO: зарегистрируйте необходимые маршруты
]
