import unittest
from datetime import date
from logic.address import Address
from logic.bill import Bill
from logic.buyer import Buyer
from logic.deliver import Deliver
from logic.person import Person
from logic.operator import Operator
from logic.supplier import Supplier


class TestDeliver(unittest.TestCase):
    deliver = Deliver()

    def test_instance(self):
        self.assertIsInstance(self.deliver, Deliver, "It's instance")

    def test_id_deliver(self):
        self.assertEqual(self.deliver.id_deliver, 1)

    def test_date(self):
        self.assertEqual(self.deliver.date, date)

    def test_buyer(self):
        self.assertIsInstance(self.deliver.buyer, Buyer)

    def test_buyer_add(self):
        self.assertIsInstance(self.deliver.buyer_add, Address)

    def test_operator(self):
        self.assertIsInstance(self.deliver.operator, Operator)

    def test_operator_add(self):
        self.assertIsInstance(self.deliver.operator_add, Address)

    def test_conveyor(self):
        self.assertIsInstance(self.deliver.conveyor, Supplier)

    def test_contact(self):
        self.assertIsInstance(self.deliver.contact, Person)

    def test_bill(self):
        self.assertIsInstance(self.deliver.bill, Bill)

    def test__str__(self):
        self.assertEqual(self.deliver.__str__(), '({0}, {1}, {2}, {3}, {4}, {5}, {6}, {7}, {8})'.format(1, date,
                                                                                                        Buyer(),
                                                                                                        Address(),
                                                                                                        Operator(),
                                                                                                        Address(),
                                                                                                        Supplier(),
                                                                                                        Person(),
                                                                                                        Bill()))


if __name__ == '__main__':
    unittest.main()
