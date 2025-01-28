# Crearemos una serie de clases que tengan las estructura de las tablas de a BD
from sqlalchemy import Column, String, Integer

from database import Base

class User(Base):
    __tablename__ = 'users'

    # columnas de mi tabla
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(30), index=True, unique=True)
    password = Column(String(30), index=True)