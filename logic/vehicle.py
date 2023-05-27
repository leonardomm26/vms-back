
class Vehicle(object):
    """
    Class used to represent a Vehicle
    """
    def __init__(self, id_vehicle: int = 1, model: str = "Model of vehicle",
                 description: str = "Description of vehicle", brand: str = "Brand of vehicle",
                 type_v: str = "Vehicle type", weight: float = 1.0, age: int = 0, price: float = 1.0,
                 status: str = "Status of vehicle"):

        """Vehicle object constructor
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
        :param status: status of the vehicle (new or second hand)
        :type status: str
        """
        self._id_vehicle = id_vehicle
        self._model = model
        self._description = description
        self._brand = brand
        self._type = type_v
        self._weight = weight
        self._age = age
        self._price = price
        self._status = status

    @property
    def id_vehicle(self) -> int:
        """Returns the id of the vehicle.
        :returns: id_vehicle of Vehicle
        :rtype: int
        """
        return self._id_vehicle

    @id_vehicle.setter
    def id_vehicle(self, id_vehicle: int):
        """The id of the vehicle.
        :param id_vehicle: id_vehicle of Vehicle.
        :type id_vehicle: int
        """
        self._id_vehicle = id_vehicle

    @property
    def model(self) -> str:
        """
        returns the model of the vehicle
        :returns model
        :rtype str
        """
        return self._model

    @model.setter
    def model(self, model: str):
        """
        sets model of the vehicle as a property
        :param model: model of the vehicle
        :type model: str

        """
        self._model = model

    @property
    def description(self) -> str:
        """Returns the description of the vehicle.
        :returns: description of Vehicle.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description: str):
        """The description of the vehicle.
        :param description: description of Vehicle.
        :type description: str
        :returns: none
        """
        self._description = description

    @property
    def status(self):
        """
        returns status of the vehicle (new or second hand)
        :return: status
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status: str):
        """
        sets status of the vehicle as a property
        :param status: status of the vehicle (new or second hand)
        :type status: str
        :return: none
        """
        self._status = status

    @property
    def brand(self) -> str:
        """
        returns brand of the vehicle
        :return: model
        :rtype: str
        """
        return self._brand

    @brand.setter
    def brand(self, brand):
        """
        sets brand of the vehicle as a property
        :param brand: vehicle's brand
        :type brand: str
        :return: none
        """
        self._brand = brand

    @property
    def type(self) -> str:
        """
        returns what type of vehicle is Vehicle
        :return: type
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type_v):
        """
        sets type of vehicle as a property
        :param type_v: what type of vehicle is
        :type type_v: str
        :return: none
        """
        self._type = type_v

    @property
    def weight(self) -> float:
        """
        returns weight of the vehicle
        :return: weight
        :rtype: float
        """
        return self._weight

    @weight.setter
    def weight(self, weight):
        """
        sets vehicle's weight as a property
        :param weight: vehicle's weight in kilograms
        :type weight: float
        :return: none
        """
        self._weight = weight

    @property
    def age(self) -> int:
        """
        returns age of the vehicle in years
        :return: age
        :rtype: int
        """
        return self._age

    @age.setter
    def age(self, age):
        """
        sets vehicle's age as a property
        :param age: vehicle's age
        :type age: int
        :return: none
        """
        self._age = age

    @property
    def price(self) -> float:
        """
        returns price of the vehicle
        :return: price
        :rtype: float
        """
        return self._price

    @price.setter
    def price(self, price):
        """
        sets price of the vehicle as a property
        :param price:
        :type price: float
        :return: none
        """
        self._price = price

    def __str__(self) -> str:
        """Returns a string of Vehicle
        :returns: string with Vehicle information.
        :rtype: str
        """
        return '({0}, {1}, {2}, {3}, {4}, {5}, {6}, {7}, {8})'.format(self._id_vehicle, self._model, self._description,
                                                                      self._brand, self._type,
                                                                      self._weight, self._age, self._price,
                                                                      self._status)

    def __eq__(self, other) -> bool:
        if isinstance(other, Vehicle):
            return (self._id_vehicle == other._id_vehicle and self._model == other._model and self._description ==
                    other._description and self._brand == other._brand and
                    self._type == other._type and self._weight == other._weight and self._age == other._age and
                    self._price == other._price and self._status == other._status)
        else:
            return False


if __name__ == '__main__':
    vehicle_1 = Vehicle(2345623, "Chevrolet Spark")
    vehicle_2 = Vehicle()

    print(vehicle_1)
    print(vehicle_2)

    if vehicle_1 == vehicle_2:
        print(f'the vehicle with id: "{vehicle_1.id_vehicle}" is equal to "{vehicle_2.id_vehicle}"')
    else:
        print(f'the vehicle with id "{vehicle_1.id_vehicle}" is different to "{vehicle_2.id_vehicle}"')
