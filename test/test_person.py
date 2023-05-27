from unittest import TestCase
from logic.person import Person
from logic.address import Address


class TestPerson(TestCase):
    person = Person(dni=123, name="Jeronimo", last_name="Pinto", contact=3155264684,
                    address=Address(), permission=0)

    def test_instance(self):
        self.assertIsInstance(self.person, Person, "Its instance!")

    def test_dni_person(self):
        self.assertEqual(self.person.dni, 123)

    def test_name(self):
        self.assertEqual(self.person.name, "Jeronimo")

    def test_last_name(self):
        self.assertEqual(self.person.last_name, "Pinto")

    def test_address(self):
        self.assertIsInstance(self.person.address, Address)

    def test_contact(self):
        self.assertEqual(self.person.contact, 3155264684)

    def test_permission(self):
        self.assertEqual(self.person.permission, 0)
