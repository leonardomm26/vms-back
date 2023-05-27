
from logic.person import Person
from logic.address import Address


class Operator(Person):
    """
        Class used to represent Operator
        """

    def __init__(self, dni: int = 1, name: str = "Name", last_name: str = "Last name", contact: int = 0,
                 address: Address = Address(), permission: int = 0, authorization: int = 0):

        """ Person constructor Operator.
        :param dni: id of Operator.
        :type dni: int
        :param name: name of Operator.
        :type name: str
        :param last_name: last name of Operator.
        :type last_name: str
        :param contact: Operator contact.
        :type contact: int
        :param address: address of Operator.
        :type address: object
        :param permission: permission of Operator.
        :type permission: int
        :param authorization: authorization of Operator.
        :type authorization: int
        :returns: Person: object
        :rtype: Person
        """
        super().__init__(dni, name, last_name, contact, address, permission)
        self.__authorization = 0 if authorization is None else authorization

    @property
    def authorization(self) -> int:
        """
        Returns authorization of Operator.
          :returns: authorization of Operator.
          :rtype: int
        """
        return self.__authorization

    @authorization.setter
    def authorization(self, authorization: int):
        """
        The permission of the Operator.
        :param authorization: permission of Operator.
        :type: int
        """
        self.__authorization = 0 if authorization is None else authorization

    def __str__(self):
        """
        Returns str of Operator.
          :returns: sting Operator
          :rtype: str
        """
        return '({0}, {1}, {2}, {3}, {4}, {5}, {6})'.format(self._dni, self._name, self._last_name, self._contact,
                                                            self._address, self._permission, self.__authorization)

    def __eq__(self, other):
        """
        returns boolean value of equivalence between two objects as buyer
        :param other: another buyer object
        :type other: Buyer
        :return: True or false
        """
        if isinstance(other, Operator):
            return super().__eq__(other) and self.__authorization == other.__authorization
        else:
            return False


if __name__ == '__main__':
    buyer = Operator(10202, name="Jeronimo", last_name="Pinto", contact=3131500, address=Address(),
                     permission=1, authorization=0)
    print(buyer.__str__())
