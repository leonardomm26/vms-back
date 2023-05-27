from logic.person import Person
from logic.address import Address
from datetime import date


class Buyer(Person):
    """
    class used to represent to buyer
    """
    def __init__(self, dni: int = 1, name: str = "Name", last_name: str = "Last name", contact: int = 1,
                 address: object = Address(), permission: int = 0, buy_date: date = date):
        """
        Buyer constructor object
        :param name: name of the buyer
        :type: str
        :param last_name: lastname of the buyer
        :type: str
        :param contact: phone of the buyer
        :type: str
        :param dni: National identity document of the buyer
        :type: int
        :param address: address of the buyer
        :type: object
        :param permission: buyer permissions
        :type: int
        """
        super().__init__(dni, name, last_name, contact, address, permission)
        self.__buy_date = date if buy_date is None else buy_date

    @property
    def buy_date(self) -> date:
        """
        Returns purchase date
        :returns: the date of purchase
        :rtype: date
        """
        return self.__buy_date

    @buy_date.setter
    def buy_date(self, buy_date: date):
        """
        The date of purchase
        :param buy_date: the date of purchase
        :type: date
        """
        self.__buy_date = date if buy_date is None else buy_date

    def __str__(self):
        """
        Return str of buyer
        :returns: string with the purchase buyer information
        :rtype: str
        """
        return '({0}, {1}, {2}, {3}, {4}, {5}, {6})'.format(self._dni, self._name, self._last_name,
                                                            self._contact, self._address, self._permission,
                                                            self.__buy_date)

    def __eq__(self, other):
        """
        returns boolean value of equivalence between two objects as buyer
        :param other: another buyer object
        :type other: Buyer
        :return: True or false
        """
        if isinstance(other, Buyer):
            return super().__eq__(other) and self.__buy_date == other.__buy_date
        else:
            return False


if __name__ == '__main__':
    buyer = Buyer(10202, name="David", last_name="Carrero", contact=3131500, address=Address(), permission=1,
                  buy_date=date.today())
    print(buyer.__str__())
