import unittest
from logic.payment_method import PaymentMethod


class TestPaymentMethod(unittest.TestCase):
    payment_method = PaymentMethod()

    def test_instance(self):
        self.assertIsInstance(self.payment_method, PaymentMethod, "It's a instance")

    def test_payment_method(self):
        self.assertEqual(self.payment_method.payment_method, "payment method")

    def test__str__(self):
        self.assertEqual(self.payment_method.__str__(), '({0})'.format("payment method"))


if __name__ == '__main__':
    unittest.main()
