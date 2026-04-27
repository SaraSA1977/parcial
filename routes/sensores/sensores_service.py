from db.db import SessionLocal
from db.models import Sensor


def save(data):
    db = SessionLocal()

    d = data["data"]

    sensor = Sensor(
        temperatura=d["temperatura"],
        humedad_ambiente=d["humedad_ambiente"],
        humedad_suelo=d["humedad_suelo"],
        led_verde=d["led_verde"],
        led_rojo=d["led_rojo"],
        led_blanco=d["led_blanco"]
    )

    db.add(sensor)
    db.commit()
    db.close()


def last():
    db = SessionLocal()
    s = db.query(Sensor).order_by(Sensor.id.desc()).first()
    db.close()

    return s.to_dict() if s else {}


def historial():
    db = SessionLocal()
    data = db.query(Sensor).all()
    db.close()

    return [d.to_dict() for d in data]


def stats():
    db = SessionLocal()
    data = db.query(Sensor).all()
    db.close()

    temps = [d.temperatura for d in data]

    return {
        "max": max(temps) if temps else 0,
        "min": min(temps) if temps else 0,
        "avg": sum(temps) / len(temps) if temps else 0
    }