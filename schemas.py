from pydantic import BaseModel

class ManufacturerSchema(BaseModel):
    name:str
    country:str
    founded_year:str

class ModelSchema(BaseModel):
    name:str
    year:str
    fuel_type:str
    transmission:str
    body_style:str
    manufacturer_id:int

class CarSchema(BaseModel):
    color:str
    vin:str
    production_year:str
    mileage:float
    price:float
    registration_date:str
    owner:str
    model_id:int