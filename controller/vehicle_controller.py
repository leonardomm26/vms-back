import json
import os
from logic.vehicle import Vehicle
PATH = os.getcwd()
DIR_DATA = PATH + '{0}data{0}'.format(os.sep)


class VehicleController(object):
    def __init__(self):
        self.file = '{0}{1}'.format(DIR_DATA, 'storage.json')

    def add(self, vehicle: Vehicle = Vehicle()) -> str:
        with open(self.file, 'r+') as f:
            data = json.load(f)
            data['vehicles'].append(vehicle.__dict__)
            print(vehicle.__str__())
            f.seek(0)
            json.dump(data, f)
        return vehicle.__str__()

    def show(self):
        with open(self.file, 'r') as file:
            json_object = json.load(file)
        return json_object

    def compare(self, value):
        with open(self.file) as f:
            data = json.load(f)
        vehicles = [vehicle for vehicle in data['vehicles'] if value in str(vehicle.values())]
        return vehicles

    def delete(self, value):
        vehicles_del = self.compare(value)
        print("Deleting:")
        for vehicle in vehicles_del:
            print(vehicle)

        with open(self.file, 'r+') as f:
            data = json.load(f)
            vehicles = data.get('vehicles', [])
            vehicles = [vehicle for vehicle in vehicles if vehicle not in vehicles_del]
            data['vehicles'] = vehicles
            f.seek(0)
            json.dump(data, f, indent=4)
            f.truncate()

        print("Deletion completed.")
        return vehicles
