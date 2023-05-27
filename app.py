import uvicorn
from fastapi import FastAPI, Query
from starlette.middleware.cors import CORSMiddleware
from controller.vehicle_controller import VehicleController
from controller.shopping_controller import ShoppingController
from logic.land_vehicle import LandVehicle
from logic.maritime_vehicle import MaritimeVehicle
from logic.air_vehicle import AirVehicle

from controller.payment_method_controller import PaymentMethodController
from logic.payment_method import PaymentMethod
import json
import os

app = FastAPI()
p_c = ShoppingController()
vh_c = VehicleController()
pm_c = PaymentMethodController()
vehicles_tb = []
origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def read_root():
    return {"200": "Welcome To Vehicle Management System"}


@app.get("/api/vehicle")
async def root():
    return vh_c.show()


@app.post("/compare_vehicle")
async def compare_vehicle(value: str = Query(...)):
    vehicles = vh_c.compare(value)
    return vehicles


@app.post("/api/land_vehicle")
async def add(id_vehicle: int, model: str, description: str, brand: str, type_v: str, weight: float, age: int,
              price: float, status: str, millage: float, cylinder_capability: float, fuel_type: str):
    if vh_c.compare(str(id_vehicle)):
        return "A vehicle with the same ID already exists"
    else:
        return vh_c.add(
            LandVehicle(id_vehicle=id_vehicle, model=model, description=description, brand=brand, type_v=type_v,
                        weight=weight, age=age, price=price, status=status, mileage=millage,
                        cylinder_capability=cylinder_capability, fuel_type=fuel_type))


@app.post("/api/maritime_vehicle")
async def add(id_vehicle: int, model: str, description: str, brand: str, type_v: str, weight: float, age: int,
              price: float, status: str, length: float, weight_capacity: float, engine_capacity: float,
              distance_travelled: float):
    if vh_c.compare(str(id_vehicle)):
        return "A vehicle with the same ID already exists"
    else:
        return vh_c.add(
            MaritimeVehicle(id_vehicle=id_vehicle, model=model, description=description, brand=brand, type_v=type_v,
                            weight=weight, age=age, price=price, status=status, length=length,
                            weight_capacity=weight_capacity, engine_capacity=engine_capacity,
                            distance_travelled=distance_travelled))


@app.post("/api/air_vehicle")
async def add(id_vehicle: int, model: str, description: str, brand: str, type_v: str, weight: float, age: int,
              price: float, status: str, flight_hours: float, people_capacity: int, engine_type: str):
    if vh_c.compare(str(id_vehicle)):
        return "A vehicle with the same ID already exists"
    else:
        return vh_c.add(
            AirVehicle(id_vehicle=id_vehicle, model=model, description=description, brand=brand, type_v=type_v,
                       weight=weight, age=age, price=price, status=status, flight_hours=flight_hours,
                       people_capacity=people_capacity, engine_type=engine_type))


@app.post("/api/delete_vehicle")
async def delete(value: int):
    vehicles = vh_c.delete(value)
    return vehicles


@app.get("/api/payment_method")
async def root():
    return pm_c.show()


@app.post("/api/payment_method")
async def add(payment_method: str):
    return pm_c.add(PaymentMethod(payment_method=payment_method))


@app.post("/api/select_payment_method")
async def select(value: str = Query(...)):
    selected_payment = pm_c.select(value)
    return selected_payment


@app.post("/api/buy")
async def buy(vehicle_id: int = Query(...)):
    vehicle = vh_c.compare(str(vehicle_id))

    if vehicle:
        vehicle_data = vehicle[0]
        if not any(v['_id_vehicle'] == vehicle_id for v in vehicles_tb):
            vehicles_tb.append({"_id_vehicle": vehicle_id, **vehicle_data})
            return {"message": "Vehicle added to purchase list."}
        else:
            return {"message": "Vehicle already added to purchase list."}
    else:
        return {"message": "Vehicle not found."}


@app.post("/api/purchase")
async def purchase(dni: str = Query(...), confirm: bool = Query(...)):
    global vehicles_tb
    if confirm:
        if not os.path.exists("data/purchase.json"):
            with open("data/purchase.json", "w") as file:
                file.write("{}")
        with open("data/purchase.json", "r") as file:
            purchase_data = json.load(file)
        if dni in purchase_data:
            for vehicle in vehicles_tb:
                if not any(v['_id_vehicle'] == vehicle['_id_vehicle'] for v in purchase_data[dni]['vehicles']):
                    purchase_data[dni]['vehicles'].append(vehicle)
        else:
            purchase_data[dni] = {"dni": dni, "vehicles": vehicles_tb}
        with open("data/purchase.json", "w") as file:
            json.dump(purchase_data, file)
        vehicles_tb.clear()
        return {"message": "Purchase done."}
    else:
        vehicles_tb.clear()
        return {"message": "Purchase cancelled."}


@app.get("/api/purchases_done")
async def get_purchases():
    purchases = p_c.show()
    return purchases


@app.post("/api/delete_purchase")
async def delete_purchase(dni: str = Query(..., description="User's DNI"),
                          id_v: str = Query(..., description="Vehicle ID")):
    purchases = p_c.erase_vehicle(dni, id_v)
    return {"message": purchases}


@app.get("/api/select_purchase")
async def select_purchase(dni: str = Query(...)):
    purchases = p_c.select(dni)
    return purchases


if __name__ == '__main__':
    uvicorn.run(app, host='localhost', port=8000, proxy_headers=True)
