from unittest import TestCase
from logic.operator import Operator


class TestOperator(TestCase):
    Operator = Operator()

    def test_instance(self):
        self.assertIsInstance(self.Operator, Operator, "it's a instance")

    def test_authorization(self):
        self.assertEqual(self.Operator.authorization, 0)
