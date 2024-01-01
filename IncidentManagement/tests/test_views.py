from django.contrib.auth.models import User
from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from incident.models import Incident


class IncidentAPITestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)

    def test_create_incident(self):
        data = {
            'incident_id': '123',
            'incident_details': 'Test incident details',
            'priority': 'High',
            'status': 'Open',
        }
        response = self.client.post('/v1/api/incidents/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Incident.objects.count(), 1)
        self.assertEqual(Incident.objects.get().reporter, self.user)

    def test_read_incident_list(self):
        incident = Incident.objects.create(
            reporter=self.user,
            incident_id='123',
            incident_details='Test incident details',
            priority='High',
            status='Open'
        )
        response = self.client.get('/v1/api/incidents/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['incident_id'], incident.incident_id)

    def test_read_incident_detail(self):
        incident = Incident.objects.create(
            reporter=self.user,
            incident_id='123',
            incident_details='Test incident details',
            priority='High',
            status='Open'
        )
        response = self.client.get(f'/v1/api/incidents/{incident.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['incident_id'], incident.incident_id)

    def test_update_incident(self):
        incident = Incident.objects.create(
            reporter=self.user,
            incident_id='123',
            incident_details='Test incident details',
            priority='High',
            status='Open'
        )
        updated_data = {
            'incident_id': '456',
            'incident_details': 'Updated incident details',
            'priority': 'Medium',
            'status': 'In progress',
        }
        response = self.client.put(f'/v1/api/incidents/{incident.id}/', updated_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Incident.objects.get().incident_id, updated_data['incident_id'])
        self.assertEqual(Incident.objects.get().priority, updated_data['priority'])
        self.assertEqual(Incident.objects.get().status, updated_data['status'])

    def test_delete_incident(self):
        incident = Incident.objects.create(
            reporter=self.user,
            incident_id='123',
            incident_details='Test incident details',
            priority='High',
            status='Open'
        )
        response = self.client.delete(f'/v1/api/incidents/{incident.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Incident.objects.count(), 0)