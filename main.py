from lector.CSV import CSV
from lector.JSON import JSON

ruta_csv = input("Ingrese la ruta del archivo CSV: ")

json = JSON()
csv = CSV()

try:
    lista_estudiantes = csv.leer_estudiantes(ruta_csv)
    ruta_json = ruta_csv.replace('.csv', '.json')
    json.escribir_estudiantes_json(lista_estudiantes, ruta_json)
    print(f"Se ha creado el archivo JSON en la ruta: {ruta_json}")
except FileNotFoundError:
    print("El archivo CSV no se encontró en la ruta especificada.")
except Exception as e:
    print(f"Ocurrió un error: {e}")
    