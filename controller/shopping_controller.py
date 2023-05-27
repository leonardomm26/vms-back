import json
import os

PATH = os.getcwd()
DIR_DATA = PATH + '{0}data{0}'.format(os.sep)


class ShoppingController(object):
    def _init_(self):
        self.file = '{0}{1}'.format(DIR_DATA, 'purchase.json')

    def get_file(self):
        return self.file

    def show(self):
        with open(self.file, 'r') as file:
            json_object = json.load(file)
        return json_object

    def select(self, value):
        with open(self.file, 'r') as file:
            data = json.load(file)
        shopping_cart = [purchase for purchase in data.values() if value in purchase["dni"]]
        return shopping_cart

    def erase_vehicle(self, dni, id_v):
        with open(self.file, "r") as file:
            data = json.load(file)
        if dni in data:
            vehicles = data[dni]["vehicles"]
            updated_vehicles = [vehicle for vehicle in vehicles if vehicle["_id_vehicle"] != int(id_v)]
            data[dni]["vehicles"] = updated_vehicles
            with open(self.file, "w") as file:
                json.dump(data, file, indent=4)
            return "The vehicle data was deleted correctly"
        return "The dni doesn't exist"

