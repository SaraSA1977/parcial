from routes.sensores import sensores_service

def insert_data(data):
    sensores_service.save(data)
    return {"msg": "ok"}


def get_last():
    return sensores_service.last()


def get_historial():
    return sensores_service.historial()


def get_stats():
    return sensores_service.stats()