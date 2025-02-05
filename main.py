# Archivi principal
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session


import crud
from database import  engine, localSession
from schemas import UserData, UserId
from models import Base

# Añadimos CORS
from fastapi.middleware.cors import CORSMiddleware

# se crean las tablas en la DB sino està creadas
Base.metadata.create_all(bind=engine)

app = FastAPI()

# añadir cors url
origins = [
    'http://localhost:5173'
]

# Añadir middlewar
app.add_middleware(
    CORSMiddleware,
    allow_origins = origins,
    allow_credentials = True, # Si falla la conexion del front, verificar esto
    allow_methods = ["*"],
    allow_headers = ["*"]
)

# Trae nuestra base de datos
def get_db():
    db = localSession()
    try:
        yield db
    finally:
        # CUando finalice la sesiòn se cierra la conexiòn
        db.close()


@app.get('/api/users', response_model=list[UserId])
def get_users(db: Session = Depends(get_db)):
    return crud.get_Users(db=db)

# Filtrado de un ùnico usuario
@app.get('/api/users/{id:int}', response_model=UserId)
def get_users(id, db:Session = Depends(get_db)):
    user_by_id = crud.get_user_by_id(db=db, id=id)
    if user_by_id:
        return user_by_id
    raise HTTPException(status_code=404, detail='Usuario no encontrado')

# Crear usuario
@app.post('/api/users/', response_model=UserId)
def create_user(user: UserData, db: Session = Depends(get_db)):
    check_name = crud.get_user_by_name(db=db, name=user.name)
    if check_name:
        raise HTTPException(status_code=404, detail="Usuario existe")
    return crud.create_user(db=db, user=user)