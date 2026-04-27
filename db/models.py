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

    created_at = Column(DateTime, default=datetime.utcnow)

    # 🔥 IMPORTANTE
    def to_dict(self):
        return {
            "id": self.id,
            "temperatura": self.temperatura,
            "humedad_ambiente": self.humedad_ambiente,
            "humedad_suelo": self.humedad_suelo,
            "led_verde": self.led_verde,
            "led_rojo": self.led_rojo,
            "led_blanco": self.led_blanco,
            "created_at": str(self.created_at)
        }