from django.urls import path
from .views import (
    PatientCreateView, PatientListView,
    HeartRateDataCreateView, HeartRateDataListView
)

urlpatterns = [
    path('', PatientListView.as_view(), name='patient-list'),
    path('add/', PatientCreateView.as_view(), name='patient-add'),
    path('heart-rate/<int:patient_id>/', HeartRateDataListView.as_view(), name='heartrate-list'),
    path('heart-rate/add/', HeartRateDataCreateView.as_view(), name='heartrate-add'),
]
