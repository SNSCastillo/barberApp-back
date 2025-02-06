from pydantic import BaseModel
from typing import Optional

# Esquema de datos que se van a pasar en fastapi
class UserSchema(BaseModel):
    nb_usuario: str
    nb_completo: str
    pass_usuario: str
    fg_activo: Optional[bool] = True

    class Config:
        from_attributes = True  # Cambié orm_mode por from_attributes

class UserResponseSchema(UserSchema):
    id_usuario: int  # Agrega id_usuario en la respuesta

    class Config:
        from_attributes = True