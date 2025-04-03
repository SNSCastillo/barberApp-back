from sqlalchemy.orm import Session
from model.user_model import User
from schema.user_schema import UserSchema

class UserCrud:
    def __init__(self, db: Session):
        self.db = db

    def create_user(self, user: UserSchema):
        db_user = User(
            nb_usuario=user.nb_usuario,
            nb_completo=user.nb_completo,
            pass_usuario=user.pass_usuario,
            fg_activo=user.fg_activo
        )
        self.db.add(db_user)
        self.db.commit()
        self.db.refresh(db_user)
        return db_user
