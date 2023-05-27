from logic.vehicle import Vehicle


class MaritimeVehicle(Vehicle):

    def __init__(self, id_vehicle: int = 1, model: str = "Model of vehicle",
                 description: str = "Description of vehicle", status: str = "Status of vehicle",
                 brand: str = "Brand of vehicle", type_v: str = "Vehicle type", weight: float = 1.0,
                 age: int = 0, price: float = 1.0, length: float = 1.0, weight_capacity: float = 1.0,
                 engine_capacity: float = 1.0, distance_travelled: float = 0.0):
        """

        :param id_vehicle: id of the maritime vehicle
        :type id_vehicle: int
        :param model: model of the maritime vehicle
        :type model: str
        :param description: description and details of the maritime vehicle
        :type description: str
        :param brand: brand the maritime vehicle belongs to
        :type brand: str
        :param type_v: category the maritime vehicle belongs to
        :type type_v: str
        :param weight: maritime vehicle's weight in kilograms
        :type weight: float
        :param age: maritime vehicle's in years
        :type age: int
        :param price: maritime vehicle's price in dollars
        :type price: float
        :param status: status of the maritime vehicle (new or second hand)
        :type status: str
        :param length: total length of the maritime vehicle from the prow to the stern
        :type length: float
        :param weight_capacity: amount of weight the maritime vehicle can bare in kilograms
        :type weight_capacity: float
        :param engine_capacity: capacity of the engine in cm^3
        :type engine_capacity: float
        :param distance_travelled: distance travelled since the first time the maritime vehicle was used in kilometers
        :type distance_travelled: float
        """
        super().__init__(id_vehicle, model, description, brand, type_v, weight, age, price, status)

        self._length = length
        self._weight_capacity = weight_capacity
        self._engine_capacity = engine_capacity
        self._distance_travelled = distance_travelled
        self._status = self.check_status()

    def check_status(self) -> str:
        """
        checks if the maritime vehicle is new or now depending on the distance travelled
        If the distance travelled is 0, the vehicle is new
        else, the vehicle is second hand
        :return: New or second hand
        :rtype: str
        """
        if self._distance_travelled == 0:
            return 'New'
        else:
            return 'Second Hand'

    @property
    def length(self) -> float:
        """
        returns the length of the maritime vehicle
        :return: length
        :rtype: float
        """
        return self._length

    @length.setter
    def length(self, length: float):
        """
        sets length of the maritime vehicle as a property
        :param length: length of the maritime vehicle from the prow to the stern in meters
        :type length: float
        :return: none
        """
        self._length = length

    @property
    def weight_capacity(self):
        """
        returns the amount of weight the maritime vehicle can bear in kilograms
        :return: weight_capacity
        :rtype: float
        """
        return self._weight_capacity

    @weight_capacity.setter
    def weight_capacity(self, weight_capacity: float):
        """
        sets the amount of weight the maritime vehicle can bear as a property
        :param weight_capacity: amount of weight
        :type weight_capacity: float
        :return: none
        """
        self._weight_capacity = weight_capacity

    @property
    def engine_capacity(self) -> float:
        """
        returns the engine capacity of the maritime vehicle
        :return: engine_capacity
        :rtype: float
        """
        return self._engine_capacity

    @engine_capacity.setter
    def engine_capacity(self, engine_capacity: float):
        """
        sets the engine capacity of the maritime vehicle as a property
        :param engine_capacity: engine capacity of the maritime vehicle
        :type engine_capacity: float
        :return: none
        """
        self._engine_capacity = engine_capacity

    @property
    def distance_travelled(self) -> float:
        """
        returns dance travelled since the maritime vehicle was used for the first time
        :return: distance_travelled
        :rtype: float
        """
        return self._distance_travelled

    @distance_travelled.setter
    def distance_travelled(self, distance_travelled: float):
        """
        sets distance travelled by the maritime vehicle as a property
        :param distance_travelled: distance travelled since the maritime vehicle was used for the first time
        :type distance_travelled: float
        :return: none
        """
        self._distance_travelled = distance_travelled

    def __str__(self) -> str:
        """Returns a string of a land vehicle
        :returns: string with land vehicle information.
        :rtype: str
        """
        return '({0}, {1}, {2}, {3}, {4}, {5}, {6}, {7}, {8}, {9}, {10}, {11}, {12})'.format(self._id_vehicle,
                                                                                             self._model,
                                                                                             self._description,
                                                                                             self._status,
                                                                                             self._brand, self._type,
                                                                                             self._weight, self._age,
                                                                                             self._price, self._length,
                                                                                             self._weight_capacity,
                                                                                             self._engine_capacity,
                                                                                             self._distance_travelled,
                                                                                             )

    def __eq__(self, other) -> bool:
        if isinstance(other, MaritimeVehicle):
            return (self._id_vehicle == other._id_vehicle and self._model == other._model and self._description ==
                    other._description and self._brand == other._brand and
                    self._type == other._type and self._weight == other._weight and self._age == other._age and
                    self._price == other._price and self._status == other._status and self._weight_capacity ==
                    other._weight_capacity and self._engine_capacity == other._engine_capacity and
                    self._distance_travelled == other._distance_travelled and self._length == other._length)
        else:
            return False


if __name__ == '__main__':
    maritime_vehicle_1 = MaritimeVehicle()
    maritime_vehicle_2 = MaritimeVehicle()
    print(maritime_vehicle_1)
    print(maritime_vehicle_2)

    if maritime_vehicle_1 == maritime_vehicle_2:
        print(f'the vehicle with id: "{maritime_vehicle_1.id_vehicle}" is equal to the vehicle with id'
              f' "{maritime_vehicle_2.id_vehicle}"')
    else:
        print(f'the vehicle with id "{maritime_vehicle_1.id_vehicle}" is different to the vehicle with id '
              f'"{maritime_vehicle_2.id_vehicle}"')
