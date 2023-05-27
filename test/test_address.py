from unittest import TestCase
from logic.address import Address


class TestAddress(TestCase):
    address = Address(house_number=7, street="San martin", apartment=1001, postal_code="00045",
                      locality="locality", department="Bolivar", country="Colombia")

    def test_instance(self):
        self.assertIsInstance(self.address, Address, "Its instance!")

    def test_house_number(self):
        self.assertEqual(self.address.house_number, 7)

    def test_street(self):
        self.assertEqual(self.address.street, "San martin")

    def test_apartment(self):
        self.assertEqual(self.address.apartment, 1001)

    def test_postal_code(self):
        self.assertEqual(self.address.postal_code, "00045")

    def test_locality(self):
        self.assertEqual(self.address.locality, "locality")

    def test_department(self):
        self.assertEqual(self.address.department, "Bolivar")

    def test_country(self):
        self.assertEqual(self.address.country, "Colombia")
