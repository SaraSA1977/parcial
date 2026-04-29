from db.db import SessionLocal  
# Importa la conexión a la base de datos (sesiones)

from db.models import Sensor  
# Importa el modelo Sensor (tabla en la BD)


def save(data):  
    # Función para guardar datos de sensores

    db = SessionLocal()  
    # Abre conexión con la base de datos

    d = data["data"]  
    # Extrae el objeto interno "data" del JSON recibido

    sensor = Sensor(
        temperatura=d["temperatura"],  # Guarda temperatura
        humedad_ambiente=d["humedad_ambiente"],  # Guarda humedad del aire
        humedad_suelo=d["humedad_suelo"],  # Guarda humedad del suelo
        led_verde=d["led_verde"],  # Estado LED verde
        led_rojo=d["led_rojo"],  # Estado LED rojo
        led_blanco=d["led_blanco"]  # Estado LED blanco
    )

    db.add(sensor)  
    # Agrega el registro a la sesión

    db.commit()  
    # Guarda los cambios en la base de datos

    db.close()  
    # Cierra la conexión


def last():  
    # Función para obtener el último dato registrado

    db = SessionLocal()  
    # Abre conexión

    s = db.query(Sensor).order_by(Sensor.id.desc()).first()  
    # Consulta el último registro (ordenado por id descendente)

    db.close()  
    # Cierra conexión

    return s.to_dict() if s else {}  
    # Convierte el objeto a diccionario (para JSON)
    # Si no hay datos, devuelve vacío


def historial():  
    # Función para obtener todos los registros

    db = SessionLocal()  
    # Abre conexión

    data = db.query(Sensor).all()  
    # Obtiene todos los datos de sensores

    db.close()  
    # Cierra conexión

    return [d.to_dict() for d in data]  
    # Convierte cada registro a diccionario y los retorna como lista


def stats():  
    # Función para calcular estadísticas de temperatura

    db = SessionLocal()  
    # Abre conexión

    data = db.query(Sensor).all()  
    # Obtiene todos los registros

    db.close()  
    # Cierra conexión

    temps = [d.temperatura for d in data]  
    # Extrae todas las temperaturas en una lista

    return {
        "max": max(temps) if temps else 0,  
        # Temperatura máxima (o 0 si no hay datos)

        "min": min(temps) if temps else 0,  
        # Temperatura mínima

        "avg": sum(temps) / len(temps) if temps else 0  
        # Promedio de temperatura
    }