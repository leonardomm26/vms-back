
class Address(object):
    """
    Class used to represent an address
    """

    def __init__(self, house_number: int = 1, apartment: int = 0, street: str = "street", postal_code: str = "00000",
                 locality: str = "locality", department: str = "department", country: str = "country"):
        """ Address constructor object.

        :param house_number: number of house.
        :type house_number: int
        :param street: name of street.
        :type street: str
        :param apartment: department of street.
        :type apartment: int
        :param postal_code: last name of city.
        :type postal_code: str
        :param locality: name of state.
        :type locality: str
        :param locality: name of state.
        :type : str
        :param department: department of the country.
        :type department: str
        :param country: name of the country.
        :type country: str
        :returns: address object
        :rtype: address
        """
        self.__house_number = 1 if house_number is None else house_number
        self.__apartment = "apartment" if apartment is None else apartment
        self.__street = "street" if street is None else street
        self.__postal_code = "00000" if postal_code is None else postal_code
        self.__locality = "locality" if locality is None else locality
        self.__department = "department" if department is None else department
        self.__country = "country" if country is None else country

    @property
    def house_number(self) -> int:
        """ Returns house number of the address.
          :returns: house number of address.
          :rtype: int
        """
        return self.__house_number

    @house_number.setter
    def house_number(self, house_number: int):
        """
        The house number of the address.
        :param house_number: house number of the address.
        :type: int
        """
        self.__house_number = 1 if house_number is None else house_number

    @property
    def apartment(self) -> int:
        """ Returns apartment number of the address.
          :returns: apartment number of address.
          :rtype: int
        """
        return self.__apartment

    @apartment.setter
    def apartment(self, apartment: int):
        """
        The apartment number of the address.
        :param apartment: apartment number of the address.
        :type: int
        """
        self.__apartment = "apartment" if apartment is None else apartment

    @property
    def street(self) -> str:
        """
        Returns the name of street of the address.
          :returns: name of street of address.
          :rtype: str
        """
        return self.__street

    @street.setter
    def street(self, street: str):
        """
        The name of street of the address.
        :param street: name of address.
        :type: str
        """
        self.__street = "street" if street is None else street

    @property
    def postal_code(self) -> str:
        """
        Returns the postal_code of the address.
          :returns: last postal_code of address.
          :rtype: str
        """
        return self.__postal_code

    @postal_code.setter
    def postal_code(self, postal_code: str):
        """
        The postal_code of the address.
        :param postal_code: postal_code of address.
        :type: str
        """
        self.__postal_code = "00000" if postal_code is None else postal_code

    @property
    def locality(self) -> str:
        """
      Returns the locality of the address.
        :returns: locality of address.
        :rtype: str
      """
        return self.__locality

    @locality.setter
    def locality(self, locality: str):
        """
        The locality of the address.
      :param locality: locality of the address
      :type: str
      """
        self.__locality = "locality" if locality is None else locality

    @property
    def department(self) -> str:
        """ Returns department of the address.
          :returns: department of address.
          :rtype: str
        """
        return self.__department

    @department.setter
    def department(self, department: str):
        """
        The department of the address.
        :param department: department of the address.
        :type: int
        """
        self.__department = "department" if department is None else department

    @property
    def country(self) -> str:
        """
        Returns the country of the address.
            :returns: country of address.
            :rtype: str
      """
        return self.__country

    @country.setter
    def country(self, country: str):
        """
        The country of the address.
      :param country: country of the address
      :type: str
      """
        self.__country = "country" if country is None else country

    def __str__(self):
        """
        Returns str of address.
          :returns: sting person
          :rtype: str
        """
        return '({0}, {1}, {2}, {3}, {4}, {5}, {6})'.format(self.__house_number, self.__apartment, self.__street,
                                                            self. __postal_code, self.__locality, self.__department,
                                                            self.__country)

    def __eq__(self, other) -> bool:
        """
        returns boolean value of equivalence between two address objects
        :param other: another address object to compare
        :type other: Address
        :return: True or False
        """
        if isinstance(other, Address):
            return (self.__house_number == other.__house_number and self.__country == other.__country and
                    self.__street == other.__country and self.__locality == other.__locality and
                    self.__apartment == other.__apartment and self.__postal_code == other.__postal_code)
        else:
            return False


if __name__ == '__main__':
    address1 = Address(house_number=7, street="San martin", apartment=1001, postal_code="00045", locality="locality",
                       department="Bolivar", country="Colombia")
    print("\nAddress:")
    address1.name = "address1"
    print(address1)

    address2 = Address()
    print(address2)
