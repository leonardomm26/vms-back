class PaymentMethod(object):
    """
    class used to represent the payment method
    """
    def __init__(self, payment_method: str = "payment method"):
        """
        Payment Method constructor object
        :param payment_method: purchase payment method
        :type: str
        """
        self.__payment_method = "payment method" if payment_method is None else payment_method

    @property
    def payment_method(self) -> str:
        """
        Returns the payment method
        :returns: purchase payment method
        :rtype: str
        """
        return self.__payment_method

    @payment_method.setter
    def payment_method(self, payment_method: str):
        """
        The purchase payment method
        :param payment_method: purchase payment method
        :type: str
        """
        self.__payment_method = "payment method" if payment_method is None else payment_method

    def __str__(self):
        """
        Return str of payment method
        :returns: string with the purchase payment method information
        :rtype: str
        """
        return '({0})'.format(self.__payment_method)

    def __eq__(self, other):
        """
        returns boolean value of equivalence between two objects as payment method
        :param other: another payment method object
        :type other: PaymentMethod
        :return: True or false
        """
        if isinstance(other, PaymentMethod):
            return self.__payment_method == other.__payment_method
        else:
            return False


if __name__ == '__main__':
    payment_method_1 = PaymentMethod("Cash")
    print(payment_method_1.__str__())
