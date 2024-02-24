from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

host_server = os.environ.get('AZURE_DB_HOST', 'localhost')
db_server_port = os.environ.get('AZURE_DB_PORT', '5432')
database_name = os.environ.get('AZURE_DB_NAME', 'cars')
db_username = os.environ.get('AZURE_DB_USERNAME', 'postgres')
db_password = os.environ.get('AZURE_DB_PASSWORD', '1234')
ssl_mode = os.environ.get('AZURE_DB_SSL_MODE', 'prefer')

DATABASE_URL = f'postgresql://{db_username}:{db_password}@{host_server}:{db_server_port}/{database_name}?sslmode={ssl_mode}'

engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
