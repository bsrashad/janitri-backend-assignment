from rest_framework import serializers
from .models import Patient, HeartRateData

# -------------------- Patient Serializer --------------------
class PatientSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = Patient
        fields = ['id', 'name', 'age', 'medical_record_number']

    def validate_age(self, value):
        if value <= 0:
            raise serializers.ValidationError("Age must be greater than zero.")
        return value

    def validate_medical_record_number(self, value):
        user = self.context['request'].user
        if Patient.objects.filter(user=user, medical_record_number=value).exists():
            raise serializers.ValidationError("This medical record number already exists for you.")
        return value


# -------------------- Heart Rate Serializer --------------------
class HeartRateDataSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    patient = PatientSerializer(read_only=True)
    patient_id = serializers.PrimaryKeyRelatedField(
        queryset=Patient.objects.all(),
        write_only=True,
        source='patient'
    )

    class Meta:
        model = HeartRateData
        fields = ['id', 'patient', 'patient_id', 'timestamp', 'heart_rate']

    def validate_heart_rate(self, value):
        if not (30 <= value <= 250):
            raise serializers.ValidationError("Heart rate must be between 30 and 250 bpm.")
        return value
