from sqlalchemy import Column, Integer, String, Boolean
from db.db import Base


class User(Base):
    __tablename__ = 'usuarios'

    id_usuario = Column(Integer, primary_key=True, index=True)
    nb_usuario = Column(String, unique=True, index=True)
    nb_completo = Column(String)
    pass_usuario = Column(String)
    fg_activo = Column(Boolean, default=True)