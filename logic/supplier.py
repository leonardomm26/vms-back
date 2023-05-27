from logic.address import Address
from logic.vehicle import Vehicle


class Supplier(object):
    """
    Class used to represent the supplier
    """
    def __init__(self, nit_supplier: int = 1, legal_name: str = 'Legal name', business_name: str = 'Business name',
                 contact: str = "0", bank_account: int = 1, address_supplier: object = Address(),
                 information_vehicle: object = Vehicle()):
        """
        Supplier constructor object
        :param nit_supplier: nit of the supplier
        :type: int
        :param legal_name: legal_name of the supplier
        :type: str
        :param business_name: business name of the supplier
        :type: str
        :param contact: information of the supplier
        :type: object
        :param bank_account: account number of the supplier
        :type: object
        :param address_supplier: supplier address
        :type: object
        :param information_vehicle: information of the vehicle
        :type: object
        """
        self.__nit_supplier = 1 if nit_supplier is None else nit_supplier
        self.__legal_name = 'Legal name' if legal_name is None else legal_name
        self.__business_name = 'Business name' if business_name is None else business_name
        self.__contact = "0" if contact is None else contact
        self.__bank__account = 1 if bank_account is None else bank_account
        self.__address_supplier = Address() if address_supplier is None else address_supplier
        self.__information_vehicle = Vehicle() if information_vehicle is None else information_vehicle

    @property
    def nit_supplier(self) -> int:
        """
        Returns the nit of the supplier
        :returns: nit of the supplier
        :rtype: int
        """
        return self.__nit_supplier

    @nit_supplier.setter
    def nit_supplier(self, nit_supplier: int):
        """
        The nit supplier method
        :param nit_supplier: nit supplier method
        type: int
        """
        self.__nit_supplier = 1 if nit_supplier is None else nit_supplier

    @property
    def legal_name(self) -> str:
        """
        Returns the legal name of the supplier
        :returns: legal name of supplier
        :rtype: int
        """
        return self.__legal_name

    @legal_name.setter
    def legal_name(self, legal_name: str):
        """
        The legal name method
        :param legal_name: nit supplier method
        type: str
        """
        self.__legal_name = 'Legal name' if legal_name is None else legal_name

    @property
    def business_name(self) -> str:
        """
        Returns the business name of the supplier
        :returns: business nam of supplier
        :rtype: str
        """
        return self.__business_name

    @business_name.setter
    def business_name(self, business_name: str):
        """
        The business name method
        :param business_name: nit supplier method
        type: str
        """
        self.__business_name = 'Business name' if business_name is None else business_name

    @property
    def contact(self) -> str:
        """
        Returns the phone number of the supplier
        :returns: the phone number of the supplier
        :rtype str
        """
        return self.__contact

    @contact.setter
    def contact(self, contact: str):
        """
        The contact method
        :param contact: phone number
        :type: str
        """
        self.__contact = "0" if contact is None else contact

    @property
    def bank_account(self) -> int:
        """
        Returns the supplier's bank account number
        :returns: supplier's bank account number
        :rtype: int
        """
        return self.__bank__account

    @bank_account.setter
    def bank_account(self, bank_account: int):
        """
        The bank account method
        :param bank_account: supplier's bank account number
        :type: int
        """
        self.__bank__account = 1 if bank_account is None else bank_account

    @property
    def address_supplier(self) -> Address():
        """
        Return the supplier's address
        :returns: supplier's address
        :rtype: object
        """
        return self.__address_supplier

    @address_supplier.setter
    def address_supplier(self, address_supplier: Address):
        """
        The supplier's address method
        :param address_supplier: supplier's address
        :type: object
        """
        self.__address_supplier = Address() if address_supplier is None else address_supplier

    @property
    def information_vehicle(self) -> Vehicle():
        """
        Returns the information of vehicle
        :returns:  the vehicle information
        :rtype: object
        """
        return self.__information_vehicle

    @information_vehicle.setter
    def information_vehicle(self, information_vehicle: Vehicle):
        """
        The vehicle information method
        :param information_vehicle: vehicle information
        :type: object
        """
        self.__information_vehicle = Vehicle() if information_vehicle is None else information_vehicle

    def __str__(self):
        """
        Return str of supplier method
        :returns: string with the supplier information
        :rtype: str
        """
        return '({0}, {1}, {2}, {3}, {4}, {5}, {6},)'.format(self.__nit_supplier, self.__legal_name, self.__business_name,
                                                             self.__contact, self.__bank__account, self.address_supplier,
                                                             self.__information_vehicle)

    def __eq__(self, other):
        """
        returns boolean value of equivalence between two objects as supplier
        :param other: another supplier object
        :type other: Supplier
        :return: True or false
        """
        return (self.__nit_supplier == other.__nit_supplier and self.__legal_name == other.__legal_name and
                self.__business_name == other.__business_name and self.__contact == other.__contact and
                self.__bank__account == other.__bank__account and
                self.__address_supplier == other.__address_supplier and
                self.__information_vehicle == other.__information_vehicle)


if __name__ == '__main__':
    supplier = Supplier(100101, 'David', 'Fast and furious', "3133202002", 31313004, Address(), Vehicle())
    print(supplier)
