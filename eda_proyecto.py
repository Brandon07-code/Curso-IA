"""
eda_proyecto.py
Script para realizar el Análisis Exploratorio de Datos (EDA) con NumPy y Matplotlib
Proyecto PAVIA: Plataforma Inteligente de Gestión del Deterioro Vial en Cartago
Asignatura: Inteligencia Artificial - COTECNOVA 2026
Estudiantes: Brandon Cortes Giraldo - Johan Sttive Linares Barragán
"""

import csv
import os
import numpy as np
import matplotlib.pyplot as plt

def cargar_datos(archivo_csv):
    """
    Carga el dataset de deterioro vial y retorna:
    - Array de NumPy con las columnas numéricas (gravedad, area_m2, costo_estimado_cop)
    - Lista completa de registros con textos y categorías
    - Lista con los encabezados
    """
    datos = []
    nombres_columnas = []
    
    try:
        with open(archivo_csv, 'r', encoding='utf-8') as archivo:
            lector = csv.reader(archivo)
            nombres_columnas = next(lector)  # Encabezados
            
            for fila in lector:
                # fila: [id, barrio, tipo_dano, gravedad, area_m2, costo_estimado_cop, prioridad]
                gravedad = float(fila[3])
                area = float(fila[4])
                costo = float(fila[5])
                datos.append([int(fila[0]), fila[1], fila[2], gravedad, area, costo, fila[6]])
                
        print(f" Datos de Cartago cargados correctamente: {len(datos)} registros viales.")
    except FileNotFoundError:
        print(f" Error: El archivo '{archivo_csv}' no existe.")
        return None, None, None
    except Exception as e:
        print(f" Error al leer el archivo: {e}")
        return None, None, None

    # Array de NumPy con solo las columnas numéricas: [gravedad, area_m2, costo_estimado_cop]
    datos_numericos = np.array([[fila[3], fila[4], fila[5]] for fila in datos], dtype=float)
    
    return datos_numericos, datos, nombres_columnas

def analizar_datos(datos_numericos):
    """
    Calcula estadísticas descriptivas vectorizadas con NumPy para cada variable numérica:
    Media, Mediana, Desviación Estándar, Mínimo y Máximo.
    """
    if datos_numericos is None or len(datos_numericos) == 0:
        return None

    # Extracción de columnas usando slicing de NumPy
    gravedades = datos_numericos[:, 0]
    areas = datos_numericos[:, 1]
    costos = datos_numericos[:, 2]

    estadisticas = {
        'gravedad_escala_1_10': {
            'media': np.mean(gravedades),
            'mediana': np.median(gravedades),
            'desviacion': np.std(gravedades),
            'minimo': np.min(gravedades),
            'maximo': np.max(gravedades)
        },
        'area_afectada_m2': {
            'media': np.mean(areas),
            'mediana': np.median(areas),
            'desviacion': np.std(areas),
            'minimo': np.min(areas),
            'maximo': np.max(areas)
        },
        'costo_reparacion_cop': {
            'total': np.sum(costos),
            'media': np.mean(costos),
            'mediana': np.median(costos),
            'desviacion': np.std(costos),
            'minimo': np.min(costos),
            'maximo': np.max(costos)
        }
    }
    return estadisticas

def generar_visualizaciones(datos_numericos, datos_completos):
    """
    Genera y guarda 3 gráficos profesionales con Matplotlib:
    1. Gráfico de barras: Costo de reparación por barrio en Cartago.
    2. Gráfico de dispersión: Relación entre Área afectada (m2) y Costo de reparación.
    3. Histograma: Distribución de los niveles de gravedad del daño vial.
    """
    if datos_numericos is None or len(datos_numericos) == 0:
        return

    gravedades = datos_numericos[:, 0]
    areas = datos_numericos[:, 1]
    costos = datos_numericos[:, 2]
    barrios = [fila[1] for fila in datos_completos]

    # 1. Gráfico de barras: Costo de reparación por barrio en Cartago
    plt.figure(figsize=(12, 6))
    colores = ['#e74c3c' if g >= 8 else '#f39c12' if g >= 5 else '#2ecc71' for g in gravedades]
    plt.bar(barrios, costos / 1000, color=colores, edgecolor='black', alpha=0.85)
    plt.title('Costo Estimado de Reparación por Barrio en Cartago (Miles de COP)', fontsize=14, fontweight='bold')
    plt.xlabel('Barrio de Cartago', fontsize=11)
    plt.ylabel('Costo de Intervención (Miles de COP)', fontsize=11)
    plt.xticks(rotation=45, ha='right', fontsize=9)
    plt.grid(True, axis='y', linestyle='--', alpha=0.5)
    plt.tight_layout()
    plt.savefig('pavia_costo_por_barrio.png', dpi=150)
    plt.close()

    # 2. Gráfico de dispersión: Área vs Costo de Reparación
    plt.figure(figsize=(8, 6))
    plt.scatter(areas, costos / 1000, color='#2980b9', s=90, alpha=0.75, edgecolors='black')
    plt.title('Relación: Área del Daño (m²) vs Costo de Reparación', fontsize=13, fontweight='bold')
    plt.xlabel('Área Afectada (m²)', fontsize=11)
    plt.ylabel('Costo Estimado (Miles de COP)', fontsize=11)
    plt.grid(True, linestyle='--', alpha=0.6)
    plt.tight_layout()
    plt.savefig('pavia_area_vs_costo.png', dpi=150)
    plt.close()

    # 3. Histograma: Distribución de la Gravedad de los Daños Viales
    plt.figure(figsize=(8, 5))
    plt.hist(gravedades, bins=6, color='#e67e22', edgecolor='black', alpha=0.8)
    plt.title('Distribución de la Severidad del Deterioro Vial en Cartago', fontsize=13, fontweight='bold')
    plt.xlabel('Nivel de Gravedad (Escala 1 a 10)', fontsize=11)
    plt.ylabel('Frecuencia (Cantidad de Reportes)', fontsize=11)
    plt.grid(True, axis='y', linestyle='--', alpha=0.6)
    plt.tight_layout()
    plt.savefig('pavia_distribucion_gravedad.png', dpi=150)
    plt.close()

def main():
    """Función principal del flujo EDA de PAVIA."""
    print("=" * 60)
    print(" ANÁLISIS EXPLORATORIO DE DATOS (EDA) CON NUMPY Y MATPLOTLIB")
    print(" PROYECTO PAVIA - CARTAGO, VALLE DEL CAUCA")
    print("=" * 60)

    ruta_csv = os.path.join('data', 'deterioro_vial_cartago.csv')
    datos_numericos, datos_completos, columnas = cargar_datos(ruta_csv)
    
    if datos_numericos is None:
        return

    # Análisis estadístico con NumPy
    estadisticas = analizar_datos(datos_numericos)
    if estadisticas:
        print("\n ESTADÍSTICAS DESCRIPTIVAS CALCULADAS CON NUMPY:")
        print("-" * 50)
        for variable, valores in estadisticas.items():
            print(f"\n>> VARIABLE: {variable.upper()}")
            for key, value in valores.items():
                if 'costo' in variable and key in ['total', 'media', 'mediana', 'minimo', 'maximo', 'desviacion']:
                    print(f"   * {key.capitalize():<12}: ${value:,.2f} COP")
                elif 'area' in variable:
                    print(f"   * {key.capitalize():<12}: {value:.2f} m²")
                else:
                    print(f"   * {key.capitalize():<12}: {value:.2f}")

    # Generación de visualizaciones
    print("\n GENERANDO VISUALIZACIONES CON MATPLOTLIB...")
    generar_visualizaciones(datos_numericos, datos_completos)
    print(" Gráficos guardados exitosamente como PNG:")
    print("   1. pavia_costo_por_barrio.png")
    print("   2. pavia_area_vs_costo.png")
    print("   3. pavia_distribucion_gravedad.png")

    print("\n Análisis EDA completado exitosamente para el Proyecto PAVIA.")

if __name__ == "__main__":
    main()
