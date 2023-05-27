from logic.vehicle import Vehicle


class LandVehicle(Vehicle):
    """
    Class used to represent a land Vehicle
    """
    def __init__(self, id_vehicle: int = 1, model: str = "Model of vehicle",
                 description: str = "Description of vehicle", status: str = "Status of vehicle",
                 brand: str = "Brand of vehicle", type_v: str = "Vehicle type", weight: float = 1.0,
                 age: int = 0, price: float = 1.0, mileage: float = 0.0, cylinder_capability: float = 0.0,
                 fuel_type: str = "Fuel type"):
        """
        LandVehicle constructor object
        :param id_vehicle: id of the vehicle
        :type id_vehicle: int
        :param model: model of the vehicle
        :type model: str
        :param description: description and details of the vehicle
        :type description: str
        :param brand: brand the vehicle belongs to
        :type brand: str
        :param type_v: category the vehicle belongs to
        :type type_v: str
        :param weight: vehicle's weight in kilograms
        :type weight: float
        :param age: vehicle's in years
        :type age: int
        :param price: vehicle's price in dollars
        :type price: float
        :param mileage: vehicle's distance travelled in kilometers
        :type mileage: float
        :param cylinder_capability: engine's cylinder capability (determines taxes)
        :type cylinder_capability: float
        :param fuel_type: kind of fuel the vehicles uses
        :type fuel_type: str
        """
        super().__init__(id_vehicle, model, description, brand, type_v, weight, age, price, status)
        self._mileage = mileage
        self._cylinder_capability = cylinder_capability
        self._fuel_type = fuel_type
        self._status = self.check_status()

    def check_status(self) -> str:
        """
        checks if the vehicle has a mileage greater than 0.0
        if mileage is greater than 0.0: car is new
        else: it is a second hand car
        :return: "New" or "Second Hand"
        :rtype: str
        """
        if self._mileage == 0.0:
            return 'New'
        else:
            return 'Second Hand'

    @property
    def mileage(self) -> float:
        """
        returns mileage of the vehicle
        :return: mileage
        :rtype: float
        """
        return self._mileage

    @mileage.setter
    def mileage(self, mileage: float):
        """
        sets vehicle's mileage as a property
        :param mileage: distance travelled in kilometers
        :type mileage: float
        :return: none
        """
        self._mileage = mileage

    @property
    def cylinder_capability(self) -> float:
        """
        returns vehicle's cylinder capability
        :return: cylinder_capability
        :rtype: float:
        """
        return self._cylinder_capability

    @cylinder_capability.setter
    def cylinder_capability(self, cylinder_capability: float):
        """
        sets vehicle's cylinder capability as a property
        :param cylinder_capability: engine's cylinder capability in cm^3
        :type cylinder_capability: float
        :return: none
        """
        self._cylinder_capability = cylinder_capability

    @property
    def fuel_type(self) -> str:
        """
        returns fuel type the vehicle uses
        :return: fuel_type
        :rtype: str
        """
        return self._fuel_type

    @fuel_type.setter
    def fuel_type(self, fuel_type: str):
        """
        sets fuel type as a property
        :param fuel_type: kind of fuel the vehicle needs
        :type fuel_type: str
        :return: none
        """
        self._fuel_type = fuel_type

    def __str__(self) -> str:
        """Returns a string of a land vehicle
        :returns: string with land vehicle information.
        :rtype: str
        """
        return '({0}, {1}, {2}, {3}, {4}, {5}, {6}, {7}, {8}, {9}, {10}, {11})'.format(self._id_vehicle, self._model,
                                                                                       self._description, self._status,
                                                                                       self._brand, self._type,
                                                                                       self._weight, self._age,
                                                                                       self._price, self._mileage,
                                                                                       self._cylinder_capability,
                                                                                       self._fuel_type)

    def __eq__(self, other) -> bool:
        """
        returns boolean value of equivalence between two objects as land vehicles
        :param other: another land vehicle object
        :type other: LandVehicle
        :return: True or false
        """
        if isinstance(other, LandVehicle):
            return (self._id_vehicle == other._id_vehicle and self._model == other._model and self._description ==
                    other._description and self._status == other._status and self._brand == other._brand and
                    self._type == other._type and self._weight == other._weight and self._age == other._age and
                    self._price == other._price and self._mileage == other._mileage and self._cylinder_capability ==
                    other._cylinder_capability and self._fuel_type == other._fuel_type)
        else:
            return False


if __name__ == '__main__':
    land_vehicle_1 = LandVehicle()
    land_vehicle_2 = LandVehicle()
    print(land_vehicle_1)
    print(land_vehicle_2)

    if land_vehicle_1 == land_vehicle_2:
        print(f'The vehicle with id "{land_vehicle_1.id_vehicle}" is equal to "{land_vehicle_2.id_vehicle}"')
    else:
        print(f'The vehicle with id "{land_vehicle_1.id_vehicle}"  is different '
              f'"{land_vehicle_2.id_vehicle}"')
