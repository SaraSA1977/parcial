from routes.sensores import sensores_service  
# Importa el service donde está la lógica real (base de datos, cálculos, etc.)


def insert_data(data):  
    # Función que recibe datos desde la ruta (request)

    sensores_service.save(data)  
    # Llama al service para guardar los datos en la base de datos

    return {"msg": "ok"}  
    # Respuesta simple al frontend indicando que todo salió bien


def get_last():  
    # Función para obtener el último dato registrado

    return sensores_service.last()  
    # Llama al service que consulta la BD y devuelve el último registro


def get_historial():  
    # Función para obtener todos los datos históricos

    return sensores_service.historial()  
    # Llama al service que devuelve todos los registros


def get_stats():  
    # Función para obtener estadísticas de los sensores

    return sensores_service.stats()  
    # Llama al service que calcula métricas (promedio, etc.)