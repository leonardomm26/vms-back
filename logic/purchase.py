from logic.buyer import Buyer
from logic.person import Person
from logic.vehicle import Vehicle


class Purchase(object):
    """
    class used to represent purchase
    """
    def __init__(self, id_purchase: int = 1, description: object = Vehicle(), cost: float = 1.0,
                 buyer: object = Buyer(), seller: object = Person()):
        """
        Purchase constructor object
        :param id_purchase: purchase identifier
        :type: int
        :param description: description of the vehicle to buy
        :type: object
        :param cost: purchase cost
        :type: float
        :param buyer: vehicle buyer information
        :type: object
        :param seller: vehicle seller information
        :type: object
        """
        self.__id_purchase = 1 if id_purchase is None else id_purchase
        self.__description = Vehicle() if description is None else description
        self.__cost = 1.0 if cost is None else cost
        self.__buyer = Buyer() if buyer is None else buyer
        self.__seller = Person() if seller is None else seller

    @property
    def id_purchase(self) -> int:
        """
        Return the purchase identifier
        :returns: the purchase identifier
        :rtype: int
        """
        return self.__id_purchase

    @id_purchase.setter
    def id_purchase(self, id_purchase: int):
        """
        The purchase identifier
        :param id_purchase: the purchase identifier
        :type: int
        """
        self.__id_purchase = 1 if id_purchase is None else id_purchase

    @property
    def description(self) -> Vehicle():
        """
        Return the information of vehicle
        :returns: the vehicle information
        :rtype: object
        """
        return self.__description

    @description.setter
    def description(self, description: Vehicle):
        """
        The description of vehicle
        :param description: the vehicle information
        :type: object
        """
        self.__description = Vehicle() if description is None else description

    @property
    def cost(self) -> float:
        """
        Returns the cost of the purchase
        :returns: cost of the purchase
        :rtype: float
        """
        return self.__cost

    @cost.setter
    def cost(self, cost: float):
        """
        The cost of the purchase
        :param cost: cost of the purchase
        :type: float
        """
        self.__cost = 1.0 if cost is None else cost

    @property
    def buyer(self) -> Buyer():
        """
        Returns the information of buyer
        :returns: the buyer information
        :rtype: object
        """
        return self.__buyer

    @buyer.setter
    def buyer(self, buyer: Buyer):
        """
        The information of buyer
        :param buyer: the buyer information
        :type: object
        """
        self.__buyer = Buyer() if buyer is None else buyer

    @property
    def seller(self) -> Person():
        """
        Returns the information of seller
        :returns: the seller information
        :rtype: object
        """
        return self.__seller

    @seller.setter
    def seller(self, seller: Person):
        """
        The information of seller
        :param seller: the seller information
        :type: object
        """
        self.__seller = Person() if seller is None else seller

    def __str__(self) -> str:
        """
        Returns str of purchase.
        :returns: string with the purchase information
        :rtype: str
        """
        return '({0}, {1}, {2}, {3}, {4})'.format(self.__id_purchase, str(self.__description),
                                                  self.__cost, str(self.__buyer), str(self.__seller))

    def __eq__(self, other):
        """
        returns boolean value of equivalence between two objects as purchase
        :param other: another purchase object
        :type other: Purchase
        :return: True or false
        """
        return (self.__id_purchase == other.__id_purchase and self.__description == other.__description and
                self.__cost == other.__cost and self.__buyer == other.__buyer and self.__seller == other.__seller)


if __name__ == '__main__':
    purchase = Purchase(10202, description=Vehicle(), cost=20000, buyer=Buyer(), seller=Person())
    print(purchase.__str__())
    print("Esto es una prueba")
