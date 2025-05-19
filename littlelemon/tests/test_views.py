from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from rest_framework import status
from restaurant.models import Menu, Booking

class MenuViewTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username="testuser", password="testpass")
        self.client.login(username="testuser", password="testpass")
        self.menu_item = Menu.objects.create(title="Burger", price=9.99, inventory=20)

    def test_menu_create_view(self):
        url = reverse('menu-list')
        data = {"title": "Pizza", "price": 12.5, "inventory": 10}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Menu.objects.count(), 2)

    def test_menu_list_view(self):
        url = reverse('menu-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], "Burger")


class BookingViewTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username="booker", password="bookpass")
        self.client.login(username="booker", password="bookpass")

        self.booking = Booking.objects.create(name="John", no_of_guests=2, booking_date="2025-06-01")

    def test_booking_list_view(self):
        url = reverse('booking-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_booking_create_view(self):
        url = reverse('booking-list')
        data = {"name": "Jane", "no_of_guests": 4, "booking_date": "2025-06-05"}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Booking.objects.count(), 2)