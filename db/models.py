from sqlalchemy import Column, Integer, Float, Boolean, String, DateTime
from datetime import datetime
from db.db import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    email = Column(String, unique=True)
    password = Column(String)


class Sensor(Base):
    __tablename__ = "sensores"

    id = Column(Integer, primary_key=True)

    temperatura = Column(Float)
    humedad_ambiente = Column(Float)
    humedad_suelo = Column(Float)

    led_verde = Column(Boolean)
    led_rojo = Column(Boolean)
    led_blanco = Column(Boolean)

    fecha = Column(DateTime, default=datetime.utcnow)