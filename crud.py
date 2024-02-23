from sqlalchemy.orm import Session
from models import Manufacturer, Model, Car
from schemas import *
from fastapi import HTTPException



# ****************************************************Manufacturer Crud started*****************************************************************

def create_manufacturer(db:Session, manufacturer:Manufacturer):
    db_manufacturer = Manufacturer(name=manufacturer.name, country=manufacturer.country, founded_year = manufacturer.founded_year)
    db.add(db_manufacturer)
    db.commit()
    db.refresh(db_manufacturer)
    return db_manufacturer


def read_all_manufacturers(db: Session):
    return db.query(Manufacturer).all()


def read_all_model(db: Session):
    return db.query(Model).all()

def read_all_cars(db: Session):
    return db.query(Car).all()


def read_manufacturer(db:Session, manufacturer_id:int):
    return db.query(Manufacturer).filter(manufacturer_id==Manufacturer.manufacturer_id).first()

def update_manufacturer(db:Session, manufacturer_id:int, manufacturer:Manufacturer):
    db_manufacturer = db.query(Manufacturer).filter(Manufacturer.manufacturer_id==manufacturer_id).first()
    db_manufacturer.name = manufacturer.name
    db_manufacturer.country = manufacturer.country
    db_manufacturer.founded_year = manufacturer.founded_year
    db.commit()
    db.refresh(db_manufacturer)
    return db_manufacturer

def delete_manufacturer(db:Session, manufacturer_id:int):
    db_manufacturer = db.query(Manufacturer).filter(Manufacturer.manufacturer_id==manufacturer_id).first()
    if not db_manufacturer:
        raise HTTPException(status_code=404,detail="user not found")
    db.delete(db_manufacturer)
    db.commit()
    return db_manufacturer


# ****************************************************Manufacturer Crud ended*****************************************************************



# ****************************************************Model Crud started*****************************************************************

def create_model(db:Session, model:Model):
    db_model = Model(name=model.name, year=model.year, fuel_type = model.fuel_type, transmission = model.transmission, body_style = model.body_style, manufacturer_id= model.manufacturer_id)
    if not db_model:
        raise HTTPException(status_code=404,detail="user not found")
    db.add(db_model)
    db.commit()
    db.refresh(db_model)
    return db_model


def read_model(db:Session, model_id:int):
    return db.query(Model).filter(model_id==Model.model_id).first()

def update_model(db:Session, model_id:int, model:Model):
    db_model = db.query(Model).filter(Model.model_id==model_id).first()
    db_model.name = model.name
    db_model.year = model.year
    db_model.fuel_type = model.fuel_type
    db_model.body_style = model.body_style
    db_model.manufacturer_id = model.manufacturer_id
    db.commit()
    db.refresh(db_model)
    return db_model

def delete_model(db:Session, model_id:int):
    db_model = db.query(Model).filter(Model.model_id==model_id).first()
    if not db_model:
        raise HTTPException(status_code=404,detail="user not found")
    db.delete(db_model)
    db.commit()
    return db_model


# ****************************************************model Crud ended*****************************************************************


# ****************************************************cars Crud started*****************************************************************

def create_cars(db:Session, car:Car):
    db_cars = Car(color=car.color, vin=car.vin, production_year = car.production_year, mileage = car.mileage, price = car.price, registration_date= car.registration_date, owner = car.owner, model_id = car.model_id)
    if not db_cars:
        raise HTTPException(status_code=404,detail="user not found")
    db.add(db_cars)
    db.commit()
    db.refresh(db_cars)
    return db_cars


def read_cars(db:Session, car_id:int):
    return db.query(Car).filter(car_id==Car.car_id).first()

def update_cars(db:Session, car_id:int, car:Car):
    db_car = db.query(Car).filter(Car.car_id==car_id).first()
    db_car.color = car.color
    db_car.vin = car.vin
    db_car.production_year = car.production_year
    db_car.mileage = car.mileage
    db_car.price = car.price
    db_car.registration_date = car.registration_date
    db_car.owner = car.owner
    db_car.model_id = car.model_id
    db.commit()
    db.refresh(db_car)
    return db_car

def delete_car(db:Session, car_id:int):
    db_car = db.query(Car).filter(Car.car_id==car_id).first()
    if not db_car:
        raise HTTPException(status_code=404,detail="user not found")
    db.delete(db_car)
    db.commit()
    return db_car



# ****************************************************cars Crud ended*****************************************************************