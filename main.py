from fastapi import FastAPI
from api import user
from model.user_model import User
from db.db import engine


# Crear las tablas al arrancar la app
User.metadata.create_all(engine)

app = FastAPI()

# Rutas de usuario
app.include_router(user.router)
