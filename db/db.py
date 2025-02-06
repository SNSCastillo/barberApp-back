import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv

# Cargar las variables de entorno
load_dotenv()

# Variables de conexión
NAME_DB = os.getenv('DB_NAME')
USER = os.getenv('USER')
PASSWORD = os.getenv('PASS')
HOST = os.getenv('DB_HOST')
PORT = os.getenv('PORT')

# Crear la cadena de conexión para SQLAlchemy
DATABASE_URL = f"postgresql+psycopg2://{USER}:{PASSWORD}@{HOST}:{PORT}/{NAME_DB}"

# Crear el motor de la base de datos (engine)
engine = create_engine(DATABASE_URL)

# Crear la sesión
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Crear la base de los modelos (Base)
Base = declarative_base()

# Función para crear las tablas
def create_tables():
    Base.metadata.create_all(bind=engine)

# Función para obtener la sesión de la base de datos
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
