from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from schema.user_schema import UserSchema, UserResponseSchema
from crud.user_crud import UserCrud
from db.db import get_db
from model.user_model import User

router = APIRouter()

@router.post("/api/insert")
async def create_user(user: UserSchema, db: Session = Depends(get_db)):
    # Verifica si el usuario ya existe
    db_user = db.query(User).filter(User.nb_usuario == user.nb_usuario).first()
    if db_user:
        raise HTTPException(status_code=400, detail="Usuario ya registrado")
    
    try:
        user_crud = UserCrud(db)
        created_user = user_crud.create_user(user)
        return {"Message": "Usuario creado exitosamente", "user": created_user}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al crear el usuario: {str(e)}")
