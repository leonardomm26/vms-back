from controller.vehicle_controller import VehicleController
import json
import os

PATH = os.getcwd()
DIR_DATA = PATH + '{0}data{0}'.format(os.sep)
vh_c = VehicleController()


class ShoppingController(object):
    def __init__(self):
        self.file = '{0}{1}'.format(DIR_DATA, 'purchase.json')

    def get_file(self):
        return self.file

    def show(self):
        with open(self.file, 'r') as file:
            json_object = json.load(file)
        return json_object

    def select(self, dni: str):
        with open(self.file, 'r') as file:
            data = json.load(file)
        shopping_cart = [purchase for purchase in data if purchase["dni"] == dni]
        return shopping_cart

    def erase_vehicle(self, dni, id_v: int):
        with open(self.file, "r") as file:
            data = json.load(file)
        if dni in [purchase["dni"] for purchase in data]:
            purchs = list(filter(lambda d: d["dni"] == dni, data))[0]
            vehicles = purchs["vehicles"]
            updated_vehicles = [vehicle for vehicle in vehicles if vehicle["id_vehicle"] != id_v]
            purchs["vehicles"] = updated_vehicles
            with open(self.file, "w") as file:
                json.dump(data, file, indent=4)
            return "The vehicle data was deleted correctly"
        return "The dni doesn't exist"

    def buy(self, dni: str, id_v: int):
        vehicle = vh_c.search(id_v)
        if vehicle:
            with open(self.file, 'r') as file:
                data = json.load(file)
                data = {dic["dni"]: dic for dic in data}
                data[dni]["vehicles"].append(vehicle)
                data = list(data.values())
                file.close()
            with open(self.file, 'w') as file:
                json.dump(data, file, indent=4)
            return {"message": "Vehicle added to purchase list."}
        else:
            return {"message": "Vehicle not found."}


if __name__ == '__main__':
    Control = ShoppingController()
    Control.show()
