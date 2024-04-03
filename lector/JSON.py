import json

class JSON:
    def __init__(self) -> None:
        pass
    
    def escribir_estudiantes_json(self, estudiantes, archivo_json):
        """Escribe una lista de objetos Estudiante en un archivo JSON."""
        estudiantes_json = []
        for estudiante in estudiantes:
            estudiante_json = {
                'id': estudiante.id,
                'nombre': estudiante.nombre,
                'apellido': estudiante.apellido
            }
            estudiantes_json.append(estudiante_json)
        
        with open(archivo_json, 'w', encoding='utf-8') as archivo:
            json.dump(estudiantes_json, archivo, indent=4)
            