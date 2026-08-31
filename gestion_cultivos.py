"""
Actividad 12 - Gestión de Cultivos
Asignatura: Inteligencia Artificial - COTECNOVA 2026
Docente: Jhon James Cano Sánchez
Estudiantes: Brandon Cortes Giraldo - Johan Sttive Linares Barragán
"""

# 1. Lista de diccionarios con datos de al menos 5 cultivos en Cartago / Valle
cultivos = [
    {"nombre": "Cafe", "hectareas": 5.0, "produccion_toneladas": 3.5},
    {"nombre": "Cana de azucar", "hectareas": 12.0, "produccion_toneladas": 10.8},
    {"nombre": "Platano", "hectareas": 4.0, "produccion_toneladas": 4.2},
    {"nombre": "Cacao", "hectareas": 3.0, "produccion_toneladas": 2.1},
    {"nombre": "Maiz", "hectareas": 6.0, "produccion_toneladas": 4.8}
]

# 2. Función para calcular el rendimiento por hectárea
def calcular_rendimiento(cultivo):
    """Calcula y retorna la producción por hectárea (ton/ha)."""
    return cultivo["produccion_toneladas"] / cultivo["hectareas"]

# 3. Función para mostrar la lista de cultivos formateada
def mostrar_cultivos(lista_cultivos):
    """Recorre la lista e imprime el nombre y rendimiento de cada cultivo."""
    print("==========================================================")
    print("           GESTION DE CULTIVOS - CARTAGO / VALLE          ")
    print("==========================================================")
    for c in lista_cultivos:
        rendimiento = calcular_rendimiento(c)
        print(f"Cultivo: {c['nombre']:<16} | Area: {c['hectareas']:>4.1f} ha | Rendimiento: {rendimiento:.2f} ton/ha")
    print("==========================================================")

# 4. Función para encontrar el cultivo con mayor rendimiento
def cultivo_mayor_rendimiento(lista_cultivos):
    """Encuentra y retorna el nombre del cultivo con mayor rendimiento."""
    if not lista_cultivos:
        return None

    mejor_cultivo = lista_cultivos[0]
    max_rendimiento = calcular_rendimiento(mejor_cultivo)

    for c in lista_cultivos[1:]:
        rend = calcular_rendimiento(c)
        if rend > max_rendimiento:
            max_rendimiento = rend
            mejor_cultivo = c

    return mejor_cultivo["nombre"]

# 5. Programa principal
def main():
    # Mostrar todos los cultivos
    mostrar_cultivos(cultivos)
    
    # Calcular y mostrar el cultivo con mayor rendimiento
    nombre_mayor = cultivo_mayor_rendimiento(cultivos)
    print(f"\n>> Cultivo con mayor rendimiento: {nombre_mayor}\n")

if __name__ == "__main__":
    main()
