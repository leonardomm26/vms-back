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

    def show(self, confirm: bool):
        with open(self.file, 'r') as file:
            if confirm:
                json_object = json.load(file)["purchases_done"]
            else:
                json_object = json.load(file)["purchases_in_shCar"]
        return json_object

    def select(self, dni: str, confirm: bool):
        with open(self.file, 'r') as file:
            data = json.load(file)
            if confirm:
                purchases = [purchase for purchase in data["purchases_done"] if purchase["dni"] == dni]
            else:
                purchases = [purchase for purchase in data["purchases_in_shCar"] if purchase["dni"] == dni]
        return purchases

    def erase_vehicle(self, dni: str, id_v: int, confirm: bool):
        vehicle = vh_c.search(id_v)
        with open(self.file, "r") as file:
            data = json.load(file)
            purchases = {dic["dni"]: dic for dic in data["purchases_done"]} if confirm else {dic["dni"]: dic for dic in
                                                                                             data["purchases_in_shCar"]}
            if dni in purchases.keys():
                if 'id_vehicle' in vehicle.keys():
                    if id_v == vehicle["id_vehicle"]:
                        purchs = purchases.get(dni)
                        vehicles = purchs["vehicles"]
                        updated_vehicles = [vehicle for vehicle in vehicles if vehicle["id_vehicle"] != id_v]
                        purchs["vehicles"] = updated_vehicles
                        if confirm:
                            data["purchases_done"] = list(purchases.values())
                        else:
                            data["purchases_in_shCar"] = list(purchases.values())
                        message = {"message": "The vehicle was deleted from your purchases correctly"}
                else:
                    message = {"message": "The vehicle not found in your purchases"}
            else:
                message = {"message": "This person doesn't has purchases"}
        with open(self.file, "w") as file:
            json.dump(data, file, indent=4)
        return message

    def purchase(self, dni: str, id_vehicle: int, confirm: bool) -> dict:
        vehicle = vh_c.search(id_vehicle)
        with open(self.file, 'r') as file:
            data = json.load(file)
            if "id_vehicle" in vehicle.keys():
                if id_vehicle == vehicle["id_vehicle"]:
                    if confirm:
                        purchases = {dic["dni"]: dic for dic in data["purchases_done"]}
                        if dni in purchases.keys():
                            purchases[dni]["vehicles"].append(vehicle)
                        else:
                            purchases[dni] = {"dni": dni, "vehicles": [vehicle]}
                        data["purchases_done"] = list(purchases.values())
                        message = {"message": "Vehicle added to purchases done"}
                    else:
                        purchases = {dic["dni"]: dic for dic in data["purchases_in_shCar"]}
                        if dni in purchases.keys():
                            if vehicle not in purchases[dni]["vehicles"]:
                                purchases[dni]["vehicles"].append(vehicle)
                                message = {"message": "Vehicle added to shopping car"}
                            else:
                                message = {"message": "The vehicle is already in the shopping cart."}
                        else:
                            purchases[dni] = {"dni": dni, "vehicles": [vehicle]}
                            message = {"message": "Vehicle added to shopping car"}
                        data["purchases_in_shCar"] = list(purchases.values())

            else:
                message = {"message": "This car is not available"}
        with open(self.file, 'w') as file:
            json.dump(data, file, indent=4)
        return message


if __name__ == '__main__':
    Control = ShoppingController()
    Control.show()
