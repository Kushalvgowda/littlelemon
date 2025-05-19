from django.test import TestCase
from restaurant.models import Menu, Booking

class MenuTest(TestCase):
    def test_get_item(self):
        item = Menu.objects.create(title="IceCream", price=20, inventory=100)
        itemstr = item.get_item()
        self.assertEqual(itemstr, "IceCream : 20")

class BookingTest(TestCase):
    def test_get_book(self):
        book = Booking.objects.create(name="Jason", no_of_guests="4", bookingdate="2025-05-20")
        bookstr = book.get_item()
        self.assertEqual(bookstr, "name : 4 : 2025-05-20")
        