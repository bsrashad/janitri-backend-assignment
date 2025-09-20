from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from users.models import User
from patients.models import Patient

class PatientTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(email="test@example.com", username="tester", password="test123")
        self.user2 = User.objects.create_user(email="other@example.com", username="other", password="test123")
        response = self.client.post('/api/users/login/', {'email': 'test@example.com', 'password': 'test123'})
        self.token = response.data['access']
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.token)

    def test_create_patient(self):
        data = {'name': 'abdullah', 'age': 24, 'medical_record_number': 'MRN123456'}
        response = self.client.post('/api/patients/add/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_patient_invalid_age(self):
        data = {'name': 'invalid', 'age': 0, 'medical_record_number': 'MRN0001'}
        response = self.client.post('/api/patients/add/', data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_duplicate_mrn(self):
        Patient.objects.create(user=self.user, name='John', age=30, medical_record_number='MRN999')
        data = {'name': 'duplicate', 'age': 22, 'medical_record_number': 'MRN999'}
        response = self.client.post('/api/patients/add/', data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_list_patients(self):
        Patient.objects.create(user=self.user, name='John', age=30, medical_record_number='MRN001')
        Patient.objects.create(user=self.user2, name='Jane', age=25, medical_record_number='MRN002')
        response = self.client.get('/api/patients/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 1)
