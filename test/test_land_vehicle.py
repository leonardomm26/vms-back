import unittest
from logic.land_vehicle import LandVehicle


class TestLandVehicle(unittest.TestCase):
    land_vehicle = LandVehicle()

    def test_instance(self):
        self.assertIsInstance(self.land_vehicle, LandVehicle, "Its instance.")

    def test_id_vehicle(self):
        self.assertEqual(self.land_vehicle.id_vehicle, 1)

    def test_model(self):
        self.assertEqual(self.land_vehicle.model, "Model of vehicle")

    def test_description(self):
        self.assertEqual(self.land_vehicle.description, "Description of vehicle")

    def test_status(self):
        self.assertEqual(self.land_vehicle.status, "New")

    def test_brand(self):
        self.assertEqual(self.land_vehicle.brand, "Brand of vehicle")

    def test_type(self):
        self.assertEqual(self.land_vehicle.type, "Vehicle type")

    def test_weight(self):
        self.assertEqual(self.land_vehicle.weight, 1.0)

    def test_age(self):
        self.assertEqual(self.land_vehicle.age, 0)

    def test_price(self):
        self.assertEqual(self.land_vehicle.price, 1.0)

    def test_mileage(self):
        self.assertEqual(self.land_vehicle.mileage, 0.0)

    def test_cylinder_capability(self):
        self.assertEqual(self.land_vehicle.cylinder_capability, 0.0)

    def test_fuel_type(self):
        self.assertEqual(self.land_vehicle.fuel_type, "Fuel type")

    def test_(self):
        self.assertEqual(self.land_vehicle.__str__(),
                         '({0}, {1}, {2}, {3}, {4}, {5}, {6}, {7}, {8}, {9}, {10}, {11})'.format(
                             1, "Model of vehicle", "Description of vehicle", "New", "Brand of vehicle", "Vehicle type",
                             1.0, 0, 1.0, 0.0, 0.0, "Fuel type"))


if __name__ == '__main__':
    unittest.main()
