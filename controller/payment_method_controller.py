import json
import os
from logic.payment_method import PaymentMethod
PATH = os.getcwd()
DIR_DATA = PATH + '{0}data{0}'.format(os.sep)


class PaymentMethodController(object):
    def __init__(self):
        self.file = '{0}{1}'.format(DIR_DATA, 'payment.json')

    def add(self, payment_method: PaymentMethod = PaymentMethod()) -> str:
        with open(self.file, 'r+') as f:
            data = json.load(f)
            data['payment_methods'].append(payment_method.__dict__)
            print(payment_method.__str__())
            f.seek(0)
            json.dump(data, f)
        f.close()
        return payment_method.__str__()

    def show(self):
        with open(self.file, 'r') as f:
            json_object = json.load(f)
        return json_object

    def select(self, value):
        with open(self.file, 'r+') as file:
            data = json.load(file)
            for payment_method in data['payment_methods']:
                if value in str(payment_method.values()):
                    return payment_method.__str__()
