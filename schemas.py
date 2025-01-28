from pydantic import BaseModel

# clases que representan esquemas para usarlo con fastapi
class UserData(BaseModel):
    name: str
    password: str

class UserId(UserData):
    id: int