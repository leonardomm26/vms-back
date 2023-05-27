import json
import os
from logic.vehicle import Vehicle
PATH = os.getcwd()
DIR_DATA = PATH + '{0}data{0}'.format(os.sep)


class VehicleController(object):
    def __init__(self):
        self.file = '{0}{1}'.format(DIR_DATA, 'storage.json')

    def show(self):
        with open(self.file, 'r') as file:
            json_object = json.load(file)["vehicles"]
        return json_object

    def add(self, vehicle: Vehicle) -> str:
        with open(self.file, 'r+') as f:
            data = json.load(f)
            if vehicle.id_vehicle not in [item['id_vehicle'] for item in data["vehicles"]]:
                data['vehicles'].append(vehicle.__dict__())
                f.seek(0)
                json.dump(data, f)
                message = vehicle.__str__()
            else:
                message = 'There is already a vehicle with that id'
        return message

    def compare(self, value):
        with open(self.file) as f:
            data = json.load(f)
        vehicles = [vehicle for vehicle in data['vehicles'] if value in str(vehicle.values())]
        return vehicles

    def delete(self, id_vehicle: int):
        with open(self.file, 'r+') as f:
            data = json.load(f)
            vehicles = data.get('vehicles', [])
            data['vehicles'] = [vehicle for vehicle in vehicles if vehicle['id_vehicle'] != id_vehicle]
            f.seek(0)
            json.dump(data, f, indent=4)
            f.truncate()
        print("Deletion completed.")
        return data['vehicles']


if __name__ == '__main__':
    Control = VehicleController()
    print(Control.show())
