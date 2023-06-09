import json
import os
from logic.payment_method import PaymentMethod
PATH = os.getcwd()
DIR_DATA = PATH + '{0}data{0}'.format(os.sep)


class PaymentMethodController(object):
    def __init__(self):
        self.file = '{0}{1}'.format(DIR_DATA, 'payment.json')

    def add(self, payment_method: PaymentMethod = PaymentMethod()) -> dict:
        with open(self.file, 'r+') as f:
            data = json.load(f)
            data["payments"].append(payment_method.__dict__())
            f.seek(0)
            json.dump(data, f, indent=4)
        return payment_method.__dict__()

    def show(self):
        with open(self.file, 'r') as f:
            json_object = json.load(f)
        return json_object

    def select(self, value):
        with open(self.file, 'r+') as file:
            data = json.load(file)
            for payment_method in data['payments']:
                if value in str(payment_method.values()):
                    return payment_method.__str__()


if __name__ == '__main__':
    Control = PaymentMethodController()
    Control.add(PaymentMethod('Metodo de pago nuevo'))

