from django.test import TestCase
from LittleLemonAPI.models import MenuItem  # Replace with your app name
from rest_framework.test import APIClient
from rest_framework import status

class MenuViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        # Create test instances of MenuItem
        MenuItem.objects.create(title="IceCream", price=80, inventory=100)
        MenuItem.objects.create(title="Burger", price=120, inventory=50)
    def test_getall(self):
        url = '/api/menu-items/'  # Use the correct API endpoint
        response = self.client.get(url)  # Make the GET request
        items = MenuItem.objects.all()
    
    # Serialize the data including id and inventory
        serialized_data = [
        {
            "id": item.id,
            "title": item.title,
            "price": str(item.price),  # Ensure price is a string
            "inventory": item.inventory
        }
        for item in items
       ]
    
    # Assertions
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json(), serialized_data)
