"""
Actividad Independiente - Clase 3
Proyecto PAVIA: Plataforma Inteligente de Gestión del Deterioro Vial en Cartago
Asignatura: Inteligencia Artificial - COTECNOVA 2026
Estudiantes: Brandon Cortes Giraldo - Johan Sttive Linares Barragán
"""

import csv
import os

def leer_datos_proyecto(ruta_csv):
    """Lee el dataset de deterioro vial y retorna una lista de diccionarios con tipos numéricos."""
    reportes = []
    with open(ruta_csv, "r", encoding="utf-8") as archivo:
        lector = csv.DictReader(archivo)
        for fila in lector:
            reporte = {
                "id": int(fila["id"]),
                "barrio": fila["barrio"],
                "tipo_dano": fila["tipo_dano"],
                "gravedad": float(fila["gravedad"]),
                "area_m2": float(fila["area_m2"]),
                "costo_estimado_cop": float(fila["costo_estimado_cop"]),
                "prioridad": fila["prioridad"]
            }
            reportes.append(reporte)
    return reportes

def calcular_estadisticas_proyecto(reportes):
    """Calcula al menos cinco estadísticas clave sobre los daños viales de Cartago."""
    total_reportes = len(reportes)
    if total_reportes == 0:
        return {}

    costos = [r["costo_estimado_cop"] for r in reportes]
    areas = [r["area_m2"] for r in reportes]
    gravedades = [r["gravedad"] for r in reportes]

    costo_total = sum(costos)
    costo_promedio = costo_total / total_reportes
    area_promedio = sum(areas) / total_reportes
    gravedad_promedio = sum(gravedades) / total_reportes
    
    max_dano_costo = max(reportes, key=lambda r: r["costo_estimado_cop"])
    total_criticos = sum(1 for r in reportes if r["prioridad"] == "Critica")
    porcentaje_criticos = (total_criticos / total_reportes) * 100

    return {
        "total_reportes": total_reportes,
        "costo_total": costo_total,
        "costo_promedio": costo_promedio,
        "area_promedio": area_promedio,
        "gravedad_promedio": gravedad_promedio,
        "max_dano_costo": max_dano_costo,
        "total_criticos": total_criticos,
        "porcentaje_criticos": porcentaje_criticos
    }

def generar_informe_proyecto(stats, archivo_salida):
    """Genera el informe detallado en formato Markdown para el proyecto PAVIA."""
    with open(archivo_salida, "w", encoding="utf-8") as archivo:
        archivo.write("# Informe de Análisis de Datos — Proyecto PAVIA\n\n")
        archivo.write("**Plataforma Inteligente para la Gestión del Deterioro Vial en Cartago, Valle del Cauca**  \n")
        archivo.write("**Autores:** Brandon Cortes Giraldo — Johan Sttive Linares Barragán  \n")
        archivo.write("**Asignatura:** Inteligencia Artificial (Semestre VI) — COTECNOVA (2026)\n\n")
        archivo.write("---\n\n")
        
        archivo.write("## 1. Descripción de los Datos\n\n")
        archivo.write("El conjunto de datos analizado contiene 15 registros georreferenciados de daños viales (huecos profundos, grietas longitudinales, hundimientos, baches y fisuras) reportados en diversos barrios representativos del municipio de Cartago (como El Prado, San Jerónimo, Zaragoza, San Nicolás, Álamos, entre otros). Cada registro incluye severidad en escala de 1 a 10, área afectada en metros cuadrados, costo estimado de reparación y nivel de prioridad asignado.\n\n")
        
        archivo.write("## 2. Estadísticas Clave del Deterioro Vial\n\n")
        archivo.write("| Métrica / Indicador | Valor Calculado |\n")
        archivo.write("|---|---|\n")
        archivo.write(f"| **Total de reportes viales analizados** | {stats['total_reportes']} reportes |\n")
        archivo.write(f"| **Costo total de intervención requerida** | ${stats['costo_total']:,.2f} COP |\n")
        archivo.write(f"| **Costo promedio por reparación** | ${stats['costo_promedio']:,.2f} COP |\n")
        archivo.write(f"| **Área promedio afectada por daño** | {stats['area_promedio']:.2f} m² |\n")
        archivo.write(f"| **Nivel de gravedad promedio** | {stats['gravedad_promedio']:.2f} / 10.0 |\n")
        archivo.write(f"| **Daño con mayor costo de reparación** | Barrio {stats['max_dano_costo']['barrio']} (${stats['max_dano_costo']['costo_estimado_cop']:,.2f} COP - {stats['max_dano_costo']['tipo_dano']}) |\n")
        archivo.write(f"| **Reportes en prioridad Crítica** | {stats['total_criticos']} ({stats['porcentaje_criticos']:.1f}%) |\n\n")
        
        archivo.write("## 3. Interpretación de los Resultados para Cartago\n\n")
        archivo.write("1. **Alta Incidencia de Daños Severos:** El promedio de gravedad de **" + f"{stats['gravedad_promedio']:.2f}/10" + "** y el hecho de que más del **" + f"{stats['porcentaje_criticos']:.1f}%" + "** de los casos estén clasificados como críticos evidencian que el deterioro en vías secundarias de Cartago requiere atención inmediata para prevenir accidentes de tránsito (especialmente en motociclistas).\n")
        archivo.write("2. **Presupuesto Focalizado:** Con un costo promedio cercano a **$" + f"{stats['costo_promedio']:,.0f} COP" + "** por punto crítico, el sistema PAVIA permite a la Secretaría de Obras Públicas priorizar los recursos financieros en los puntos de mayor impacto social antes de que el daño aumente su área y costo de bacheo.\n")
        archivo.write("3. **Utilidad para Modelos de IA:** Estos datos estructurados servirán como línea base para entrenar los modelos de Visión por Computadora (YOLOv8) y Machine Learning predictivo en las siguientes fases del curso.\n")

if __name__ == "__main__":
    ruta_dataset = os.path.join("data", "deterioro_vial_cartago.csv")
    reportes = leer_datos_proyecto(ruta_dataset)
    estadisticas = calcular_estadisticas_proyecto(reportes)
    generar_informe_proyecto(estadisticas, "informe_proyecto.md")
    print("Informe de PAVIA generado exitosamente: informe_proyecto.md")
