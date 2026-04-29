import os  # Permite acceder a variables del sistema (.env)
from dotenv import load_dotenv  # Carga variables de entorno desde el archivo .env
from sqlalchemy import create_engine  # Permite crear la conexión con la base de datos
from sqlalchemy.orm import sessionmaker, declarative_base  # Manejo de sesiones y base del ORM

#accede a la info del .env
load_dotenv()  # Carga las variables del archivo .env

DATABASE_URL = os.getenv("DB_URL")  
# Obtiene la URL de conexión a la base de datos desde .env

print(DATABASE_URL)  
# Imprime la URL (útil para debug, ⚠️ en producción no se recomienda)

engine = create_engine(
    DATABASE_URL
)  
# Crea el motor de conexión a la base de datos (SQLAlchemy)

SessionLocal = sessionmaker(
    autocommit=False,  # No guarda cambios automáticamente
    autoflush=False,  # No envía cambios automáticamente
    bind=engine  # Vincula la sesión con el motor de la BD
)
# Fábrica de sesiones → cada vez que llamas SessionLocal() obtienes una conexión

Base = declarative_base()  
# Base del ORM → de aquí heredan todos los modelos (User, Sensor)

print("Connected to DB OK")  
# Mensaje para confirmar que la configuración se ejecutó

from db import models  
# 👈 Importa los modelos para que SQLAlchemy los reconozca

Base.metadata.create_all(bind=engine)  
# Crea las tablas en la base de datos si no existen