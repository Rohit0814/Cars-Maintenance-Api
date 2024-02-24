
# Cars-Maintenance-Api

The "Cars-Maintenance-Api" is a web API designed for managing information related to cars, manufacturers, and models. It utilizes a PostgreSQL database to store and retrieve data. The database consists of three main tables: "manufacturers," "models," and "cars."


<p align="center">
  <img src = https://github.com/Rohit0814/Cars-Maintenance-Api/blob/main/images%20(1).jpeg?raw=true width=50%>
</p>

<!--![Logo](https://github.com/Rohit0814/Cars-Maintenance-Api/blob/main/images%20(1).jpeg?raw=true)-->


## Installation

Require Software to execute

```bash
  Python 3

  PostgreSQL

```
    
## Run Locally

Clone the project

```bash
  git clone https://github.com/Rohit0814/Cars-Maintenance-Api.git
```

Go to the project directory

```bash
  cd Cars-Maintenance-Api
```

Install dependencies

```bash
  pip install fastapi

  pip install sqlalchemy

  pip install database

  pip install "uvicorn[standard]"
```

Start the server

```bash
   uvicorn main:app --reload
```


## Api Views

**Manufacturer**<br>
<p align="center">
  <img src = https://github.com/Rohit0814/Cars-Maintenance-Api/blob/main/M1.png?raw=true width=50%>
<!-- ![App Screenshot](https://github.com/Rohit0814/Cars-Maintenance-Api/blob/main/M1.png?raw=true) -->
</p>


**Model**<br>
<p align="center">
  <img src = https://github.com/Rohit0814/Cars-Maintenance-Api/blob/main/MODEL1.png?raw=true width=50%>
<!-- ![App Screenshot](https://github.com/Rohit0814/Cars-Maintenance-Api/blob/main/MODEL1.png?raw=true) -->
</p>


**Cars**<br>
<p align="center">
  <img src = https://github.com/Rohit0814/Cars-Maintenance-Api/blob/main/CAR1.png?raw=true width=50%>
<!-- ![App Screenshot](https://github.com/Rohit0814/Cars-Maintenance-Api/blob/main/CAR1.png?raw=true) -->
</p>

## Features

* #### FastAPI Framework ####
    * Utilizes the FastAPI framework in Python for building the API.
    * FastAPI simplifies API development with automatic OpenAPI and JSON Schema generation.


* #### PostgreSQL Database ####
    * Uses PostgreSQL as the database management system for storing and managing data.
    * Leverages relational database capabilities for efficient data organization.


* #### Endpoints ####
    * Provides endpoints for creating, retrieving, updating, and deleting data related to manufacturers, models, and cars.
    * Implements CRUD (Create, Read, Update, Delete) operations for each entity.


* #### Data Validation ####
    * Utilizes Pydantic models for data validation, ensuring that the incoming data adheres to the specified schema.


* #### Relationships ####
    * Implements relationships between tables using foreign keys, linking manufacturers to models and models to cars.


* #### Error Handling ####
    * Includes error handling mechanisms, such as HTTPException, to provide meaningful responses in case of errors or invalid requests.


* #### Security Considerations ####
    * Incorporates secure coding practices to protect against common web vulnerabilities.
    * Implements proper authentication and authorization mechanisms if required.


* #### Deployment ####
    * Can be deployed on a server or cloud platform, allowing for scalability and accessibility.

## Important url




**Manufacturer**
![App Screenshot](https://github.com/Rohit0814/Cars-Maintenance-Api/blob/main/pic1.png?raw=true)

**Model**
![App Screenshot](https://github.com/Rohit0814/Cars-Maintenance-Api/blob/main/pic2.png?raw=true)

**Cars**
![App Screenshot](https://github.com/Rohit0814/Cars-Maintenance-Api/blob/main/pic3.png?raw=true)


## Support

For support, email singhrohit.rs747@gmail.com or join our Slack channel.

