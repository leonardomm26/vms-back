import unittest
from logic.supplier import Supplier
from logic.supplier import Address
from logic.vehicle import Vehicle


class TestSupplier(unittest.TestCase):
    supplier = Supplier()

    def test_instance(self):
        return self.assertIsInstance(self.supplier, Supplier, "It's a instance")

    def test_nit_supplier(self):
        return self.assertEqual(self.supplier.nit_supplier, 1)

    def test_legal_name(self):
        return self.assertEqual(self.supplier.legal_name, 'Legal name')

    def test_business_name(self):
        return self.assertEqual(self.supplier.business_name, 'Business name')

    def test_contact(self):
        return self.assertEqual(self.supplier.contact, "0")

    def test_bank_account(self):
        return self.assertEqual(self.supplier.bank_account, 1)

    def test_address_supplier(self):
        return self.assertIsInstance(self.supplier.address_supplier, Address)

    def test_information_vehicle(self):
        return self.assertIsInstance(self.supplier.information_vehicle, Vehicle)

    def test__str__(self):
        return self.assertEqual(self.supplier.__str__(), '({0}, {1}, {2}, {3}, {4}, {5}, {6},)'.format(1, 'Legal name',
                                                                                                       'Business name',
                                                                                                       "0", 1,
                                                                                                       Address(),
                                                                                                       Vehicle()))


if __name__ == '__main__':
    unittest.main()
