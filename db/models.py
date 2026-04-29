from sqlalchemy import Column, Integer, Float, Boolean, String, DateTime  
# Importa los tipos de datos para definir las columnas de la base de datos

from datetime import datetime  # Manejo de fechas (aunque aquí no se usa directamente)
from db.db import Base  # Base del ORM (de aquí heredan los modelos)
from sqlalchemy.sql import func  # Permite usar funciones SQL como NOW()


class User(Base):  
    # Modelo que representa la tabla "users" en la base de datos

    __tablename__ = "users"  
    # Nombre de la tabla en la BD

    id = Column(Integer, primary_key=True)  
    # ID único del usuario (clave primaria)

    email = Column(String, unique=True)  
    # Email del usuario (único, no se puede repetir)

    password = Column(String)  
    # Contraseña del usuario (⚠️ almacenada en texto plano)


class Sensor(Base):  
    # Modelo que representa la tabla "sensores"

    __tablename__ = "sensores"  
    # Nombre de la tabla

    id = Column(Integer, primary_key=True)  
    # ID único del registro

    temperatura = Column(Float)  
    # Valor de temperatura

    humedad_ambiente = Column(Float)  
    # Humedad del ambiente

    humedad_suelo = Column(Float)  
    # Humedad del suelo

    led_verde = Column(Boolean)  
    # Estado del LED verde (encendido/apagado)

    led_rojo = Column(Boolean)  
    # Estado del LED rojo

    led_blanco = Column(Boolean)  
    # Estado del LED blanco

    created_at = Column(DateTime, server_default=func.now())  
    # Fecha de creación automática (la pone la BD con la hora actual)

    # 🔥 IMPORTANTE
    def to_dict(self):  
        # Método para convertir el objeto a diccionario (para enviarlo como JSON)

        return {
            "id": self.id,  # ID del registro
            "temperatura": self.temperatura,  # Temperatura
            "humedad_ambiente": self.humedad_ambiente,  # Humedad ambiente
            "humedad_suelo": self.humedad_suelo,  # Humedad suelo
            "led_verde": self.led_verde,  # Estado LED verde
            "led_rojo": self.led_rojo,  # Estado LED rojo
            "led_blanco": self.led_blanco,  # Estado LED blanco
            "created_at": str(self.created_at)  # Fecha convertida a string para JSON
        }