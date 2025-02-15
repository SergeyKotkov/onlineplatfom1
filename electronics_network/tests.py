from django.test import TestCase
from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
from .models import NetworkNode
from django.contrib.auth.models import User

class NetworkNodeModelTests(TestCase):
    def setUp(self):
        self.node = NetworkNode.objects.create(
            name="Test Node",
            email="test@example.com",
            country="Country",
            city="City",
            street="Street",
            house_number="1",
            product_name="Product",
            product_model="Model",
            release_date="2023-10-01",
            level=1
        )

    def test_node_creation(self):
        self.assertEqual(self.node.name, "Test Node")
        self.assertEqual(self.node.debt, 0)

    def test_node_str_representation(self):
        self.assertEqual(str(self.node), "Test Node")

class NetworkNodeViewSetTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.node = NetworkNode.objects.create(
            name="Test Node",
            email="test@example.com",
            country="Country",
            city="City",
            street="Street",
            house_number="1",
            product_name="Product",
            product_model="Model",
            release_date="2023-10-01",
            level=1
        )
        self.client.force_authenticate(user=self.user)

    def test_list_nodes(self):
        url = reverse('networknode-list')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_create_node(self):
        url = reverse('networknode-list')
        data = {
            "name": "New Node",
            "email": "new@example.com",
            "country": "Country",
            "city": "City",
            "street": "Street",
            "house_number": "2",
            "product_name": "Product",
            "product_model": "Model",
            "release_date": "2023-10-01",
            "level": 1
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(NetworkNode.objects.count(), 2)

    def test_retrieve_node(self):
        url = reverse('networknode-detail', args=[self.node.id])
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], 'Test Node')

    def test_update_node(self):
        url = reverse('networknode-detail', args=[self.node.id])
        data = {
            "name": "Updated Node",
            "email": "updated@example.com",
            "country": "Country",
            "city": "City",
            "street": "Street",
            "house_number": "1",
            "product_name": "Product",
            "product_model": "Model",
            "release_date": "2023-10-01",
            "level": 1
        }
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.node.refresh_from_db()
        self.assertEqual(self.node.name, 'Updated Node')

    def test_delete_node(self):
        url = reverse('networknode-detail', args=[self.node.id])
        response = self.client.delete(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(NetworkNode.objects.count(), 0)