from pydantic import BaseModel
from typing import Optional

class UserSchema(BaseModel):
    nb_usuario: str
    nb_completo: str
    pass_usuario: str
    fg_activo: Optional[bool] = True

    class Config:
        from_attributes = True

class UserResponseSchema(UserSchema):
    id_usuario: int

    class Config:
        from_attributes = True
