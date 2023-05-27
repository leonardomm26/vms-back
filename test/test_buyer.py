import unittest
from datetime import date
from logic.address import Address
from logic.buyer import Buyer
from test_person import TestPerson


class TestBuyer(TestPerson):
    buyer = Buyer()

    def test_instance(self):
        self.assertIsInstance(self.buyer, Buyer, "it's a instance")

    def test_buy_date(self):
        self.assertEqual(self.buyer.buy_date, date)

    def test__str__(self):
        self.assertEqual(self.buyer.__str__(), '({0}, {1}, {2}, {3}, {4}, {5}, {6})'.format(1, "Name", "Last name",
                                                                                            1, Address(), 0, date))


if __name__ == '__main__':
    unittest.main()
