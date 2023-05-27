import unittest
from logic.air_vehicle import AirVehicle


class TestAirVehicle(unittest.TestCase):
    air_vehicle = AirVehicle()

    def test_instance(self):
        self.assertIsInstance(self.air_vehicle, AirVehicle, "Its instance.")

    def test_id_vehicle(self):
        self.assertEqual(self.air_vehicle.id_vehicle, 1)

    def test_model(self):
        self.assertEqual(self.air_vehicle.model, "Model of vehicle")

    def test_description(self):
        self.assertEqual(self.air_vehicle.description, "Description of vehicle")

    def test_status(self):
        self.assertEqual(self.air_vehicle.status, "New")

    def test_brand(self):
        self.assertEqual(self.air_vehicle.brand, "Brand of vehicle")

    def test_type(self):
        self.assertEqual(self.air_vehicle.type, "Vehicle type")

    def test_weight(self):
        self.assertEqual(self.air_vehicle.weight, 1.0)

    def test_age(self):
        self.assertEqual(self.air_vehicle.age, 0)

    def test_price(self):
        self.assertEqual(self.air_vehicle.price, 1.0)

    def test_flight_hours(self):
        self.assertEqual(self.air_vehicle.flight_hours, 0.0)

    def test_people_capacity(self):
        self.assertEqual(self.air_vehicle.people_capacity, 1)

    def test_engine_type(self):
        self.assertEqual(self.air_vehicle.engine_type, "Engine type")

    def test_(self):
        self.assertEqual(self.air_vehicle.__str__(),
                         '({0}, {1}, {2}, {3}, {4}, {5}, {6}, {7}, {8}, {9}, {10}, {11})'.format(
                             1, "Model of vehicle", "Description of vehicle", "New", "Brand of vehicle", "Vehicle type",
                             1.0, 0, 1.0, 0.0, 1, "Engine type"))


if __name__ == '__main__':
    unittest.main()
