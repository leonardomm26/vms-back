from logic.address import Address


class Person(object):
    """
    Class used to represent a Person
    """

    def __init__(self, dni: int = 1, name: str = "Name", last_name: str = "Last name", contact: int = 0,
                 address: object = Address(), permission: int = 0):

        """ Person constructor object.
        :param dni: id of person.
        :type dni: int
        :param name: name of person.
        :type name: str
        :param last_name: last name of person.
        :type last_name: str
        :param contact: person contact.
        :type contact: int
        :param address: address of person
        :type address: object
        :param permission: permission of person
        :type permission: int
        :returns: Person: object
        :rtype: Person
        """
        self._dni = 1 if dni is None else dni
        self._name = "Name" if name is None else name
        self._last_name = "Last name" if last_name is None else last_name
        self._contact = 0 if contact is None else contact
        self._address = Address() if address is None else address
        self._permission = 0 if permission is None else permission

    @property
    def dni(self) -> int:
        """
        Returns dni of the person.
          :returns: dni of person.
          :rtype: int
        """
        return self._dni

    @dni.setter
    def dni(self, dni: int):
        """
        The id of the person.
        :param dni: id of person.
        :type: int
        """
        self._dni = 1 if dni is None else dni

    @property
    def name(self) -> str:
        """ Returns the name of the person.
          :returns: name of person.
          :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name: str):
        """ The name of the person.
        :param name: name of person.
        :type: str
        """
        self._name = "Name" if name is None else name

    @property
    def last_name(self) -> str:
        """ Returns the last name of the person.
          :returns: last name of person.
          :rtype: str
        """
        return self._last_name

    @last_name.setter
    def last_name(self, last_name: str):
        """ The last name of the person.
        :param last_name: last name of person.
        :type: str
        """
        self._last_name = "Last name" if last_name is None else last_name

    @property
    def contact(self) -> int:
        """
        Returns the contact of the person.
        :returns: contact of person.
        :rtype: int
      """
        return self._contact

    @contact.setter
    def contact(self, contact: int):
        """
        The contact of the person.
        :param contact: contact of the person
        :type: int
        """
        self._contact = 0 if contact is None else contact

    @property
    def address(self) -> Address():
        """
        Returns address of the person.
          :returns: address of person.
          :rtype: object
        """
        return self._address

    @address.setter
    def address(self, address: Address):
        """
        The address of the person.
        :param address: address of person.
        :type: object
        """
        self._address = Address() if address is None else address

    @property
    def permission(self) -> int:
        """
        Returns permission of the person.
          :returns: permission of person.
          :rtype: int
        """
        return self._permission

    @permission.setter
    def permission(self, permission: int):
        """
        The permission of the person.
        :param permission: permission of person.
        :type: int
        """
        self._permission = 0 if permission is None else permission

    def __str__(self):
        """
        Returns str of person.
          :returns: sting person
          :rtype: str
        """
        return '({0}, {1}, {2}, {3}, {4}, {5})'.format(self._dni, self._name, self._last_name, self._contact,
                                                       self._address, self._permission)

    def __eq__(self, other):
        """
        returns boolean value of equivalence between two objects as person
        :param other: another person object
        :type other: Person
        :return: True or false
        """
        return (self._dni == other._dni and self._name == other._name and
                self._last_name == other._last_name and self._address == other._address and
                self._permission == other._permission)


if __name__ == '__main__':
    person_1 = Person(dni=1234567890, name="Luis", last_name="Pinto", contact=3155264684,
                      address=Address(), permission=1)
    person_2 = Person(dni=1234567890)
    print(person_1)
    print(person_2)

    if person_1.dni == person_2.dni:
        print(f'The person with id "{person_1.dni}" is equal to the person with id "{person_2.dni}"')
    else:
        print(f'The person with id "{person_1.dni}" is different to the person with id "{person_2.dni}"')
