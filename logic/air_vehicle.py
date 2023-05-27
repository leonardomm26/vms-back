from logic.vehicle import Vehicle


class AirVehicle(Vehicle):
    """
    Class used to represent an air vehicle
    """

    def __init__(self, id_vehicle: int = 1, model: str = "Model of vehicle",
                 description: str = "Description of vehicle", status: str = "Status of vehicle",
                 brand: str = "Brand of vehicle", type_v: str = "Vehicle type", weight: float = 1.0,
                 age: int = 0, price: float = 1.0, flight_hours: float = 0.0, people_capacity: int = 1,
                 engine_type: str = "Engine type"):
        """
        Air vehicle constructor object
        :param id_vehicle: id of air vehicle
        :type id_vehicle: int
        :param model: model of air vehicle
        :type model: str
        :param description: descriptions and details of the air vehicle
        :type description: str
        :param status: status of the air vehicle (new or second hand)
        :type status: str
        :param brand: brand the air vehicle belongs to
        :type brand: str
        :param type_v: kind of air vehicle it is
        :type type_v: str
        :param weight: air vehicle's weight
        :type weight: float
        :param age: air vehicle's age
        :type age: int
        :param price: price in dollars of the air vehicle
        :type price: float
        :param flight_hours: hours the air vehicle has flown
        :type flight_hours: float
        :param people_capacity: amount of people the air vehicle can bare
        :type people_capacity: int
        :param engine_type: kind of  engine the air vehicle got
        :type engine_type: str
        """

        super().__init__(id_vehicle, model, description, brand, type_v, weight, age, price, status)

        self._flight_hours = flight_hours
        self._people_capacity = people_capacity
        self._engine_type = engine_type
        self._status = self.check_status()

    def check_status(self) -> str:
        """
        checks if the air vehicle is new or now by its flight hours
        if the vehicle has no flight hours, it is new
        else. the vehicle is second hand
        :return: New or Second Hand
        :rtype: str
        """
        if self._flight_hours == 0:
            return 'New'
        else:
            return 'Second Hand'

    @property
    def flight_hours(self) -> float:
        """
        returns the flight hours of the air vehicle
        :return: flight_hours
        :rtype: float
        """
        return self._flight_hours

    @flight_hours.setter
    def flight_hours(self, flight_hours: float):
        """
        sets the flight hours of the air vehicle as a property
        :param flight_hours: amount of hours the air vehicle has flown
        :type flight_hours: float
        :return: None
        """
        self._flight_hours = flight_hours

    @property
    def people_capacity(self) -> int:
        """
        returns amount of people the air vehicle can bare
        :return: people_capacity
        :rtype: int
        """
        return self._people_capacity

    @people_capacity.setter
    def people_capacity(self, people_capacity: int):
        """
        sets amount of people the air vehicle can bare as a property
        :param people_capacity: amount of people the air vehicle can bare
        :type people_capacity: int
        :return: none
        """
        self._people_capacity = people_capacity

    @property
    def engine_type(self) -> str:
        """
        returns kind of engine the air vehicle uses as a property
        :return: engine_type
        :rtype: str
        """
        return self._engine_type

    @engine_type.setter
    def engine_type(self, engine_type: str):
        """
        sets the kind of engine the air vehicle uses as a property
        :param engine_type: kind of engine the air vehicle uses
        :type engine_type: str
        :return: none
        """
        self._engine_type = engine_type

    def __str__(self) -> str:
        """Returns a string of a land vehicle
        :returns: string with land vehicle information.
        :rtype: str
        """
        return '({0}, {1}, {2}, {3}, {4}, {5}, {6}, {7}, {8}, {9}, {10}, {11})'.format(self._id_vehicle, self._model,
                                                                                       self._description, self._status,
                                                                                       self._brand, self._type,
                                                                                       self._weight, self._age,
                                                                                       self._price, self._flight_hours,
                                                                                       self._people_capacity,
                                                                                       self._engine_type)

    def __eq__(self, other) -> bool:
        """
        returns boolean value of equivalence between two air vehicle objects
        :param other: another air vehicle object to compare
        :type other: AirVehicle
        :return: True or False
        """
        if isinstance(other, AirVehicle):
            return (self._id_vehicle == other._id_vehicle and self._model == other._model and self._description ==
                    other._description and self._brand == other._brand and
                    self._type == other._type and self._weight == other._weight and self._age == other._age and
                    self._price == other._price and self._status == other._status and self._flight_hours ==
                    other._flight_hours and self._people_capacity == other._people_capacity and
                    self._engine_type == other._engine_type)
        else:
            return False


if __name__ == '__main__':
    air_vehicle_1 = AirVehicle()
    air_vehicle_2 = AirVehicle()
    print(air_vehicle_1)
    print(air_vehicle_1)

    if air_vehicle_1 == air_vehicle_2:
        print(f'The vehicle with id "{air_vehicle_1.id_vehicle}" '
              f'is equal to the vehicle with id "{air_vehicle_2.id_vehicle}"')
    else:
        print(f'The vehicle with id "{air_vehicle_1.id_vehicle}" is different to the vehicle '
              f'"{air_vehicle_2.id_vehicle}"')
