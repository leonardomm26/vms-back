from logic.buyer import Buyer
from logic.purchase import Purchase
from logic.address import Address
from logic.payment_method import PaymentMethod
from logic.person import Person


class Bill(object):
    """
    class used to represent a Bill
    """
    def __init__(self, id_bill: int = 1, description_purchase: object = Purchase(), seller: object = Person(),
                 buyer: object = Buyer(), address_buyer: object = Address(), payment_method: object = PaymentMethod()):
        """
        Bill constructor object
        :param id_bill: id of bill
        :type id_bill: int
        :param description_purchase: description purchase
        :type description_purchase purchase
        :param seller: seller
        :type seller: object
        :param buyer: buyer
        :type buyer: object
        :param address_buyer: address buyer
        :type address_buyer: object
        :param payment_method: payment method
        :type payment_method: object
        :returns: Bill object
        :rtype: Bill
        """

        self.__id_bill = 1 if id_bill is None else id_bill
        self.__description_purchase = Purchase() if description_purchase is None else description_purchase
        self.__seller = Person() if seller is None else seller
        self.__buyer = Buyer() if buyer is None else buyer
        self.__address_buyer = Address() if address_buyer is None else address_buyer
        self.__payment_method = PaymentMethod() if payment_method is None else payment_method

    @property
    def id_bill(self) -> int:
        """
        Returns id bill of the bill.
        :returns: id bill of the bill.
        :rtype: int
        """
        return self.__id_bill

    @id_bill.setter
    def id_bill(self, id_bill: int):
        """
        The id bill of the bill.
        :param id_bill: id bill of the bill.
        :type: int
        """
        self.__id_bill = 1 if id_bill is None else id_bill

    @property
    def description_purchase(self) -> Purchase():
        """
        Return vehicle purchase description
        :returns: description purchase
        :rtype: object
        """
        return self.__description_purchase

    @description_purchase.setter
    def description_purchase(self, description_purchase: Purchase):
        """
        The vehicle purchase description
        :param description_purchase: description purchase
        :type: object
        """
        self.__description_purchase = Purchase() if description_purchase is None else description_purchase

    @property
    def seller(self) -> Person():
        """
        Return seller of vehicle
        :returns: seller
        :rtype: object
        """
        return self.__seller

    @seller.setter
    def seller(self, seller: Person):
        """
        The seller of vehicle
        :param seller: seller
        :type: object
        """
        self.__seller = Person() if seller is None else seller

    @property
    def buyer(self) -> Buyer():
        """
        Return buyer of vehicle
        :returns: buyer
        :rtype: object
        """
        return self.__buyer

    @buyer.setter
    def buyer(self, buyer: Buyer):
        """
        The buyer of vehicle
        :param buyer: buyer
        :type: object
        """
        self.__buyer = Buyer() if buyer is None else buyer

    @property
    def address_buyer(self) -> Address():
        """
        Return address buyer
        :returns: address_buyer
        :rtype: object
        """
        return self.__address_buyer

    @address_buyer.setter
    def address_buyer(self, address_buyer: Address):
        """
        The purchaser's address
        :param address_buyer: buyer's address
        :type: object
        """
        self.__address_buyer = Address() if address_buyer is None else address_buyer

    @property
    def payment_method(self) -> PaymentMethod():
        """
        Return payment method for the purchase
        :returns: payment_method
        :rtype: object
        """
        return self.__payment_method

    @payment_method.setter
    def payment_method(self, payment_method: PaymentMethod):
        """
        The payment method
        :param payment_method: the method of payment for the purchase
        :type: object
        """
        self.__payment_method = PaymentMethod() if payment_method is None else payment_method

    def __str__(self):
        """
        Returns str of bill.
        :returns: string with the invoice information
        :rtype: str
        """
        return '({0}, {1}, {2}, {3}, {4}, {5})'.format(self.__id_bill, self.__description_purchase, self.__seller,
                                                       self.__buyer, self.__address_buyer, self.__payment_method)

    def __eq__(self, other) -> bool:
        """
        returns boolean value of equivalence between two objects as bill
        :param other: another bill object
        :type other: Bill
        :return: True or false
        """
        if isinstance(other, Bill):
            return (self.__id_bill == other.__id_bill and
                    self.__description_purchase == other.__description_purchase and self.__seller == other.__seller and
                    self.__buyer == other.__buyer and self.__address_buyer == other.__address_buyer and
                    self.__payment_method == other.__payment_method)
        else:
            return False


if __name__ == '__main__':
    bill_1 = Bill(10202, "heavy vehicles", Person(), Buyer(), Address(), PaymentMethod())
    print(bill_1.__str__())
