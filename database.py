from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from dotenv import load_dotenv
import os

# Cargammos las variables de entorno
load_dotenv()

# Constante que llamen a las variables de entorno
DB_NAME = os.getenv('DB_NAME')
DB_HOST = os.getenv('DB_HOST')
DB_DIALECT = os.getenv('DB_DIALECT')
DB_PASS = os.getenv('DB_PASSWORD')
DB_USER = os.getenv('DB_USER')


# <tipo de base de datos>+<se conecta mediante el módulo pymysql>://<usuario que se va a conectar a la BD>:<contraseña>@<localhost>/<nombre de la BD>
URLCONNECTION = '{}://{}:{}@{}/{}'.format(DB_DIALECT, DB_USER, DB_PASS, DB_HOST, DB_NAME)

engine = create_engine(URLCONNECTION)

# Autoflus: Actualiza cada commit que se haga
localSession = sessionmaker(autoflush=False, autocommit=False, bind=engine)

Base = declarative_base()