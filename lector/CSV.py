import csv
from lector.Estudiante import Estudiante

class CSV:
    def __init__(self) -> None:
        pass
    
    def leer_estudiantes(self, archivo_csv):
        """Lee un archivo CSV con información de estudiantes y devuelve una lista de objetos Estudiante."""
        estudiantes = []
        with open(archivo_csv, newline='', encoding='utf-8') as archivo:
            lector_csv = csv.reader(archivo)
            next(lector_csv)  # Omitir la primera línea (encabezados)
            for fila in lector_csv:
                id, nombre, apellido = fila
                estudiantes.append(Estudiante(id, nombre, apellido))
        return estudiantes
    