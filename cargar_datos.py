"""
Actividad 13 - Carga y Procesamiento de Datos (Proyecto PAVIA)
Asignatura: Inteligencia Artificial - COTECNOVA 2026
Docente: Jhon James Cano Sánchez
Estudiantes: Brandon Cortes Giraldo - Johan Sttive Linares Barragán
"""

import csv
import os

# 1. Función para leer datos de un archivo CSV y convertirlos en lista de diccionarios
def leer_datos(ruta_archivo):
    """
    Lee un archivo CSV y retorna una lista de diccionarios
    con los tipos de datos numéricos convertidos.
    """
    if not os.path.exists(ruta_archivo):
        print(f"Error: El archivo no existe en la ruta {ruta_archivo}")
        return []

    lista_datos = []
    with open(ruta_archivo, mode='r', encoding='utf-8') as archivo:
        lector_csv = csv.DictReader(archivo)
        for fila in lector_csv:
            # Convertimos los campos numéricos para poder operar con ellos
            registro = {
                "id": int(fila["id"]),
                "barrio": fila["barrio"],
                "tipo_dano": fila["tipo_dano"],
                "gravedad": float(fila["gravedad"]),
                "area_m2": float(fila["area_m2"]),
                "costo_estimado_cop": float(fila["costo_estimado_cop"]),
                "prioridad": fila["prioridad"]
            }
            lista_datos.append(registro)

    return lista_datos

# 2. Función para mostrar el resumen estadístico de los datos cargados
def mostrar_resumen(datos):
    """
    Muestra la cantidad de registros y al menos 3 estadísticas básicas
    calculadas con funciones y estructuras de Python.
    """
    if not datos:
        print("No hay datos disponibles para mostrar el resumen.")
        return

    total_registros = len(datos)
    
    # Extracción de columnas numéricas en listas
    costos = [d["costo_estimado_cop"] for d in datos]
    areas = [d["area_m2"] for d in datos]
    gravedades = [d["gravedad"] for d in datos]

    # Cálculos estadísticos
    promedio_costo = sum(costos) / total_registros
    area_maxima = max(areas)
    area_minima = min(areas)
    promedio_gravedad = sum(gravedades) / total_registros

    # Daños críticos
    criticos = sum(1 for d in datos if d["prioridad"] == "Critica")

    print("==========================================================")
    print("      RESUMEN DE DATOS - PROYECTO PAVIA (CARTAGO)         ")
    print("==========================================================")
    print(f"Total de reportes viales cargados: {total_registros}")
    print("----------------------------------------------------------")
    print("Estadisticas clave:")
    print(f"1. Costo promedio de reparacion:   ${promedio_costo:,.2f} COP")
    print(f"2. Area maxima de dano:            {area_maxima:.2f} m2")
    print(f"3. Area minima de dano:            {area_minima:.2f} m2")
    print(f"4. Nivel de gravedad promedio:     {promedio_gravedad:.2f} / 10.0")
    print(f"5. Total de reportes criticos:     {criticos} de {total_registros}")
    print("==========================================================")

# 3. Programa principal
def main():
    ruta = os.path.join("data", "deterioro_vial_cartago.csv")
    print(f"Cargando dataset desde: {ruta}...\n")
    
    reportes = leer_datos(ruta)
    mostrar_resumen(reportes)

if __name__ == "__main__":
    main()
