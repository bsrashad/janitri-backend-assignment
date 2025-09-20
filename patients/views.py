from rest_framework import generics, permissions, filters, status
from rest_framework.response import Response
from rest_framework.exceptions import PermissionDenied
from rest_framework.pagination import PageNumberPagination
from .models import Patient, HeartRateData
from .serializers import PatientSerializer, HeartRateDataSerializer

class StandardResultsSetPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100


# -------------------- Patient APIs --------------------

class PatientCreateView(generics.CreateAPIView):
    """
    POST /api/patients/add/
    Create a new patient for the authenticated user.
    """
    serializer_class = PatientSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class PatientListView(generics.ListAPIView):
    """
    GET /api/patients/
    Listing  all patients of the authenticated user (paginated).
    """
    serializer_class = PatientSerializer
    permission_classes = [permissions.IsAuthenticated]
    pagination_class = StandardResultsSetPagination

    def get_queryset(self):
        return Patient.objects.filter(user=self.request.user).order_by('id')


# -------------------- Heart Rate APIs --------------------

class HeartRateDataCreateView(generics.CreateAPIView):
    """
    POST /api/patients/heart-rate/add/
    Create a heart rate record. Only allowed for the owner of the patient.
    """
    serializer_class = HeartRateDataSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        patient = serializer.validated_data['patient']
        if patient.user != self.request.user:
            raise PermissionDenied("You cannot add data for this patient.")
        serializer.save()


class HeartRateDataListView(generics.ListAPIView):
    """
    GET /api/patients/heart-rate/<patient_id>/
    List heart rate records for a patient. Only accessible by the owner.
    Supports pagination and ordering by timestamp.
    """
    serializer_class = HeartRateDataSerializer
    permission_classes = [permissions.IsAuthenticated]
    pagination_class = StandardResultsSetPagination
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['timestamp']
    ordering = ['-timestamp']

    def get_queryset(self):
        patient_id = self.kwargs.get('patient_id')
        try:
            patient = Patient.objects.get(id=patient_id)
        except Patient.DoesNotExist:
            raise PermissionDenied("Patient not found.")

        if patient.user != self.request.user:
            raise PermissionDenied("You cannot access this patient's data.")

        #shows patients heart rate data in descending order (latest data comes first)
        return HeartRateData.objects.filter(patient_id=patient_id).order_by('-timestamp') 
