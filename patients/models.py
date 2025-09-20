from django.db import models
from django.conf import settings

class Patient(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='patients')
    name = models.CharField(max_length=255)
    age = models.PositiveIntegerField()
    medical_record_number = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class HeartRateData(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='heart_rates')
    timestamp = models.DateTimeField(auto_now_add=True)
    heart_rate = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.patient.name} - {self.heart_rate} bpm at {self.timestamp}"
