import unittest
from logic.purchase import Purchase
from logic.bill import Bill
from logic.person import Person
from logic.buyer import Buyer
from logic.address import Address
from logic.payment_method import PaymentMethod


class TestBill(unittest.TestCase):
    bill = Bill()

    def test_instance(self):
        self.assertIsInstance(self.bill, Bill, "It's instance.")

    def test_id_bill(self):
        self.assertEqual(self.bill.id_bill, 1)

    def test_description_purchase(self):
        self.assertIsInstance(self.bill.description_purchase, Purchase)

    def test_seller(self):
        self.assertIsInstance(self.bill.seller, Person)

    def test_buyer(self):
        self.assertIsInstance(self.bill.buyer, Buyer)

    def test_address_buyer(self):
        self.assertIsInstance(self.bill.address_buyer, Address)

    def test_payment_method(self):
        self.assertIsInstance(self.bill.payment_method, PaymentMethod)

    def test__str__(self):
        self.assertEqual(self.bill.__str__(), '({0}, {1}, {2}, {3}, {4}, {5})'.format(1, Purchase().__str__(),
                                                                                      Person().__str__(),
                                                                                      Buyer().__str__(),
                                                                                      Address().__str__(),
                                                                                      PaymentMethod().__str__()))


if __name__ == '__main__':
    unittest.main()
