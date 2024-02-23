from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class Manufacturer(Base):
    __tablename__ = "manufacturer"
    manufacturer_id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    country = Column(String, index=True)
    founded_year = Column(String, index=True)
    
    models = relationship("Model", back_populates="manufacturer")

class Model(Base):
    __tablename__ = "model"
    model_id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    year = Column(String, index=True)
    fuel_type = Column(String, index=True)
    transmission = Column(String, index=True)
    body_style = Column(String, index=True)
    manufacturer_id = Column(Integer, ForeignKey('manufacturer.manufacturer_id'), index=True)
    
    manufacturer = relationship("Manufacturer", back_populates="models")
    cars = relationship("Car", back_populates="model")

class Car(Base):
    __tablename__ = "car"
    car_id = Column(Integer, primary_key=True, index=True)
    color = Column(String, index=True)
    vin = Column(String,index=True)
    production_year = Column(String,index=True)
    mileage = Column(Float,index=True)
    price = Column(Float,index=True)
    registration_date = Column(String,index=True)
    owner = Column(String,index=True)
    model_id = Column(Integer, ForeignKey('model.model_id'), index=True)
    
    model = relationship("Model", back_populates="cars")

