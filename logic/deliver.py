from logic.buyer import Buyer
from datetime import date
from logic.address import Address
from logic.person import Person
from logic.supplier import Supplier
from logic.bill import Bill
from logic.operator import Operator


class Deliver(object):
    """
    class used to represent the delivery
    """
    def __init__(self, id_deliver: int = 1, date_t: date = date, buyer: object = Buyer(),
                 buyer_add: object = Address(), operator: object = Operator(), operator_add: object = Address(),
                 conveyor: object = Supplier(), contact: object = Person(), bill: object = Bill()):
        """
        Deliver constructor object
        :param id_deliver: id deliver
        :type id_deliver: int
        :param date_t: delivery date
        :type date_t: datetime
        :param buyer: vehicle buyer
        :type buyer: object
        :param buyer_add: vehicle buyer's address
        :type buyer_add: object
        :param operator: vehicle edition operator
        :type operator: object
        :param operator_add: the address of the operator
        :type operator_add: object
        :param conveyor: the vehicle conveyor
        :type conveyor: object
        :param contact: contact information
        :type contact: object
        :param bill: the purchase bill
        :type bill: object
        """
        self.__id_deliver = 1 if id_deliver is None else id_deliver
        self.__date = date if date_t is None else date_t
        self.__buyer = Buyer() if buyer is None else buyer
        self.__buyer_add = Address() if buyer_add is None else buyer_add
        self.__operator = Operator() if operator is None else operator
        self.__operator_add = Address() if operator_add is None else operator_add
        self.__conveyor = Supplier() if conveyor is None else conveyor
        self.__contact = Person() if contact is None else contact
        self.__bill = Bill() if bill is None else bill

    @property
    def id_deliver(self) -> int:
        """
        Returns id deliver
        :return: id_deliver
        :rtype: int
        """
        return self.__id_deliver

    @id_deliver.setter
    def id_deliver(self, id_deliver: int):
        """
        The id deliver
        :param id_deliver: the id_deliver
        :type id_deliver: int
        """
        self.__id_deliver = 1 if id_deliver is None else id_deliver

    @property
    def date(self) -> date:
        """
        Returns the deadline
        :returns: deadline
        :rtype: datetime
        """
        return self.__date

    @date.setter
    def date(self, date_t):
        """
        The deadline
        :param date_t: deadline
        :type date_t: datetime
        """
        self.__date = date if date is None else date_t

    @property
    def buyer(self) -> Buyer():
        """
        Returns the buyer information
        :returns: the buyer information
        :rtype: object
        """
        return self.__buyer

    @buyer.setter
    def buyer(self, buyer: Buyer):
        """
        The buyer information
        :param buyer: the buyer information
        :type: object
        """
        self.__buyer = Buyer() if buyer is None else buyer

    @property
    def buyer_add(self) -> Address():
        """
        Returns the address buyer
        :returns: the buyer address
        :rtype: object
        """
        return self.__buyer_add

    @buyer_add.setter
    def buyer_add(self, buyer_add: Address):
        """
        The address buyer
        :param buyer_add: the buyer address
        :type: object
        """
        self.__buyer_add = Address() if buyer_add is None else buyer_add

    @property
    def operator(self) -> Operator():
        """
        Returns the information operator
        :returns: the information operator
        :rtype: object
        """
        return self.__operator

    @operator.setter
    def operator(self, operator: Operator):
        """
        The operator information
        :param operator: the operator information
        :type: object
        """
        self.__operator = Operator() if operator is None else operator

    @property
    def operator_add(self) -> Address:
        """
        Returns the direction of the operator
        :returns: the address of the operator
        :rtype: object
        """
        return self.__operator_add

    @operator_add.setter
    def operator_add(self, operator_add: Address):
        """
        The direction of the operator
        :param operator_add: address of the operator
        :type: object
        """
        self.__operator_add = Address() if operator_add is None else operator_add

    @property
    def conveyor(self) -> Supplier():
        """
        Return the information of conveyor
        :returns: the conveyor data
        :rtype: object
        """
        return self.__conveyor

    @conveyor.setter
    def conveyor(self, conveyor: Supplier):
        """
        The information of conveyor
        :param conveyor: the conveyor data
        :type: object
        """
        self.__conveyor = Supplier() if conveyor is None else conveyor

    @property
    def contact(self) -> Person:
        """
        Returns the information of contact
        :returns: the contact data
        :rtype: object
        """
        return self.__contact

    @contact.setter
    def contact(self, contact: Person):
        """
        The information of contact
        :param contact: the contact data
        :type: object
        """
        self.__contact = Person() if contact is None else contact

    @property
    def bill(self) -> Bill():
        """
        Returns the purchase bill
        :returns: the purchase bill
        :rtype: object
        """
        return self.__bill

    @bill.setter
    def bill(self, bill: Bill):
        """
        The purchase bill
        :param bill: the purchase bill
        :type: object
        """
        self.__bill = Bill() if bill is None else bill

    def __str__(self):
        """
        Returns str of deliver
        :returns: string with the delivery information
        :rtype: str
        """
        return '({0}, {1}, {2}, {3}, {4}, {5}, {6}, {7}, {8})'.format(self.__id_deliver, self.__date, self.__buyer,
                                                                      self.__buyer_add, self.__operator,
                                                                      self.__operator_add,
                                                                      self.__conveyor, self.__contact, self.__bill)

    def __eq__(self, other) -> bool:
        """
        returns boolean value of equivalence between two objects as deliver
        :param other: another deliver object
        :type other: Deliver
        :return: True or false
        """
        if isinstance(other, Deliver):
            return (self.__id_deliver == other.__id_deliver and
                    self.__date == other.__date and self.__buyer == other.__buyer and
                    self.__buyer_add == other.__buyer_add and self.__operator == other.__operator and
                    self.__operator_add == other.__operator_add and self.__conveyor == other.conveyor and
                    self.__contact == other.__contact and self.__bill == other.__bill)
        else:
            return False


if __name__ == '__main__':
    deliver_1 = Deliver(12020, date.today(), Buyer(), Address(), Operator(), Address(), Supplier(), Person(), Bill())
    deliver_2 = Deliver(12022, date.today(), Buyer(), Address(), Operator(), Address(), Supplier(), Person(), Bill())
    print("\nDeliver1: ")
    print(deliver_1.__str__())

    print(deliver_1.__eq__(deliver_2))
