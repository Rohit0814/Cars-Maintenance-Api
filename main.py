from fastapi import FastAPI,Depends,HTTPException
from sqlalchemy.orm import Session
from database import *
from schemas import ManufacturerSchema, ModelSchema, CarSchema
from crud import *
app = FastAPI()

Base.metadata.create_all(bind=engine)

def get_db():
    db=SessionLocal()
    try:
        yield db
    finally:
        db.close()


# ****************************************************Manufacturer Crud started*****************************************************************


@app.post("/manufacturer/create")
async def create_manufacturer_api(user: ManufacturerSchema, db: Session = Depends(get_db)):
    return create_manufacturer(db, user)

@app.get("/manufacturer")
async def read_all_manufacturers_route(db: Session = Depends(get_db)):
    db_manufacturers = read_all_manufacturers(db)
    if not db_manufacturers:
        raise HTTPException(status_code=404, detail="Manufacturers not found")
    return db_manufacturers


@app.get("/manufacturer/{manufacturer_id}")
async def read_manufacturer_api(manufacturer_id: int , db: Session = Depends(get_db)):
    db_manufacturer = read_manufacturer(db, manufacturer_id)
    if db_manufacturer is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_manufacturer

@app.put("/manufacturer/update/{manufacturer_id}")
async def update_manufacturer_api(manufacturer_id: int, user: ManufacturerSchema, db: Session = Depends(get_db)):
    db_manufacturer = update_manufacturer(db, manufacturer_id, user)
    if db_manufacturer is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_manufacturer

@app.delete("/manufacturer/delete/{user_id}")
async def delete_user_api(manufacturer_id: int, db: Session = Depends(get_db)):
    db_manufacturer = delete_manufacturer(db, manufacturer_id)
    if db_manufacturer is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_manufacturer


# ****************************************************Manufacturer Crud ended*****************************************************************


# ****************************************************Model Crud started************************************************************************



@app.post("/model/create")
async def create_model_api(model: ModelSchema, db: Session = Depends(get_db)):
    return create_model(db, model)


@app.get("/model")
async def read_all_model_route(db: Session = Depends(get_db)):
    db_model = read_all_model(db)
    if not db_model:
        raise HTTPException(status_code=404, detail="Models not found")
    return db_model

@app.get("/model/{model_id}")
async def read_model_api(model_id: int , db: Session = Depends(get_db)):
    db_model = read_model(db, model_id)
    if db_model is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_model

@app.put("/model/update/{model_id}")
async def update_model_api(model_id: int, model: ModelSchema, db: Session = Depends(get_db)):
    db_model = update_model(db, model_id, model)
    if db_model is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_model

@app.delete("/model/delete/{model_id}")
async def delete_model_api(model_id: int, db: Session = Depends(get_db)):
    db_model = delete_model(db, model_id)
    if db_model is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_model


# ****************************************************Model Crud ended************************************************************************


# ****************************************************Cars Crud Started*************************************************************************

@app.post("/cars/create")
async def create_cars_api(cars: CarSchema, db: Session = Depends(get_db)):
    return create_car(db, cars)


@app.get("/cars")
async def read_all_car_route(db: Session = Depends(get_db)):
    db_car = read_all_cars(db)
    if not db_car:
        raise HTTPException(status_code=404, detail="Users not found")
    return db_car

@app.get("/cars/{car_id}")
async def read_car_api(car_id: int , db: Session = Depends(get_db)):
    db_car = read_cars(db, car_id)
    if db_car is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_car

@app.put("/cars/update/{car_id}")
async def update_car_api(car_id: int, cars: CarSchema, db: Session = Depends(get_db)):
    db_car = update_cars(db, car_id, cars)
    if db_car is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_car

@app.delete("/cars/delete/{car_id}")
async def delete_car_api(car_id: int, db: Session = Depends(get_db)):
    db_car = delete_car(db, car_id)
    if db_car is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_car


# ****************************************************Cars Crud ended************************************************************************