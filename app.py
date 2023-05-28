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

app = FastAPI()
p_c = ShoppingController()
vh_c = VehicleController()
pm_c = PaymentMethodController()
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
async def compare_vehicle(value: str = Query(..., description="Keyword")):
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


@app.post("/api/purchase")
async def purchase(dni: str = Query(..., description="User's DNI"),
                   id_vehicle: int = Query(..., description="Vehicle ID"),
                   confirm: bool = Query(..., description="Purchase State")):
    return p_c.purchase(dni, id_vehicle, confirm)


@app.get("/api/purchases_done")
async def get_purchases():
    purchases = p_c.show(True)
    return purchases


@app.get("/api/shopping_car")
async def get_purchases():
    purchases = p_c.show(False)
    return purchases


@app.post("/api/delete_purchase")
async def delete_purchase(dni: str = Query(..., description="User's DNI"),
                          id_v: int = Query(..., description="Vehicle ID"),
                          confirm: bool = Query(..., description="Purchase State")):
    return p_c.erase_vehicle(dni, id_v, confirm)


@app.get("/api/select_purchase")
async def select_purchase(dni: str = Query(..., description="User's DNI"),
                          confirm: bool = Query(..., description="Purchase State")):
    purchases = p_c.select(dni, confirm)
    return purchases


if __name__ == '__main__':
    uvicorn.run(app, host='localhost', port=8000, proxy_headers=True)
