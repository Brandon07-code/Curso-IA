"""
preparacion_datos_pavia.py
Script de preprocesamiento, análisis exploratorio con Pandas y Seaborn,
y preparación de datos para Machine Learning del proyecto PAVIA.

Proyecto: PAVIA (Plataforma Inteligente para la Gestión del Deterioro Vial en Cartago)
Asignatura: Inteligencia Artificial - COTECNOVA
Docente: Jhon James Cano Sánchez
Estudiantes: Brandon Cortes Giraldo & Johan Sttive Linares Barragán
"""

import os
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

def cargar_datos(archivo_csv):
    """
    Carga el dataset vial desde un archivo CSV y retorna un DataFrame de Pandas.
    """
    try:
        df = pd.read_csv(archivo_csv)
        print(f"[OK] Datos cargados correctamente: {df.shape[0]} registros y {df.shape[1]} columnas.")
        return df
    except FileNotFoundError:
        print(f"[ERROR] No se encontro el archivo: '{archivo_csv}'")
        return None
    except Exception as e:
        print(f"[ERROR] Error al leer el archivo CSV: {e}")
        return None

def explorar_datos(df):
    """
    Realiza la inspección inicial del DataFrame:
    primeras filas, tipos de datos, estadísticas y conteo de valores nulos.
    """
    print("\n" + "=" * 65)
    print("1. EXPLORACIÓN INICIAL DE LOS DATOS (PANDAS)")
    print("=" * 65)
    
    print("\n--- PRIMERAS 5 FILAS (df.head()) ---")
    print(df.head())
    
    print("\n--- INFORMACIÓN GENERAL DE LAS COLUMNAS (df.info()) ---")
    df.info()
    
    print("\n--- ESTADÍSTICAS DESCRIPTIVAS NUMÉRICAS (df.describe()) ---")
    print(df.describe())
    
    print("\n--- CONTEO DE VALORES NULOS POR COLUMNA (df.isnull().sum()) ---")
    nulos = df.isnull().sum()
    print(nulos)
    if nulos.sum() == 0:
        print(">> El dataset no presenta valores nulos; la integridad estructural es del 100%.")

def limpiar_y_transformar_datos(df):
    """
    Maneja valores nulos y aplica Feature Engineering creando columnas derivadas:
    1. costo_por_m2: Costo estimado por metro cuadrado de bacheo.
    2. indice_criticidad: Ponderación matemática entre gravedad (1-10) y superficie (m2).
    """
    print("\n" + "=" * 65)
    print("2. LIMPIEZA Y TRANSFORMACIÓN DE DATOS (FEATURE ENGINEERING)")
    print("=" * 65)
    
    df_transformado = df.copy()
    
    # Verificación preventiva de nulos en variables numéricas
    for col in ['gravedad', 'area_m2', 'costo_estimado_cop']:
        if df_transformado[col].isnull().any():
            mediana = df_transformado[col].median()
            df_transformado[col] = df_transformado[col].fillna(mediana)
            print(f">> Valores nulos en '{col}' imputados con la mediana: {mediana}")
            
    # Columna derivada 1: Costo unitario por m2
    df_transformado['costo_por_m2'] = df_transformado['costo_estimado_cop'] / df_transformado['area_m2']
    print("[+] Columna derivada creada: 'costo_por_m2' (Costo por metro cuadrado)")
    
    # Columna derivada 2: Índice de criticidad ponderado
    df_transformado['indice_criticidad'] = df_transformado['gravedad'] * df_transformado['area_m2']
    print("[+] Columna derivada creada: 'indice_criticidad' (Gravedad * Área m²)")
    
    print("\n--- MUESTRA DEL DATAFRAME CON COLUMNAS DERIVADAS ---")
    print(df_transformado[['barrio', 'tipo_dano', 'gravedad', 'area_m2', 'costo_por_m2', 'indice_criticidad', 'prioridad']].head())
    
    return df_transformado

def generar_visualizaciones_seaborn(df, ruta_salida="."):
    """
    Genera y guarda 3 visualizaciones estadísticas avanzadas con Seaborn:
    1. Histograma con curva KDE para el costo estimado de reparación.
    2. Diagrama de caja (Boxplot) para comparar el costo por tipo de daño.
    3. Gráfico de dispersión con línea de regresión (Área vs Costo).
    """
    print("\n" + "=" * 65)
    print("3. GENERACIÓN DE VISUALIZACIONES AVANZADAS CON SEABORN")
    print("=" * 65)
    
    sns.set_theme(style="whitegrid", font_scale=1.1)
    
    # -------------------------------------------------------------
    # 1. Histograma y Curva de Densidad (KDE) de Costos
    # -------------------------------------------------------------
    plt.figure(figsize=(10, 6))
    sns.histplot(
        data=df,
        x='costo_estimado_cop',
        bins=8,
        kde=True,
        color='#0d9488',
        edgecolor='black'
    )
    plt.title('Distribución del Costo Estimado de Reparación en Cartago', fontsize=14, weight='bold', pad=15)
    plt.xlabel('Costo Estimado de Reparación (COP)', fontsize=12)
    plt.ylabel('Frecuencia de Daños', fontsize=12)
    plt.tight_layout()
    img1 = os.path.join(ruta_salida, 'pavia_distribucion_costo_seaborn.png')
    plt.savefig(img1, dpi=150)
    plt.close()
    print(f"[OK] Gráfico 1 guardado: {img1}")
    
    # -------------------------------------------------------------
    # 2. Boxplot (Diagrama de Caja): Costo según Tipo de Daño
    # -------------------------------------------------------------
    plt.figure(figsize=(11, 6))
    sns.boxplot(
        data=df,
        x='tipo_dano',
        y='costo_estimado_cop',
        palette='Set2',
        hue='tipo_dano',
        legend=False
    )
    plt.title('Dispersión del Costo de Reparación por Tipo de Daño', fontsize=14, weight='bold', pad=15)
    plt.xlabel('Tipo de Daño Vial', fontsize=12)
    plt.ylabel('Costo Estimado (COP)', fontsize=12)
    plt.xticks(rotation=20, ha='right')
    plt.tight_layout()
    img2 = os.path.join(ruta_salida, 'pavia_boxplot_costo_tipo_dano.png')
    plt.savefig(img2, dpi=150)
    plt.close()
    print(f"[OK] Gráfico 2 guardado: {img2}")
    
    # -------------------------------------------------------------
    # 3. Regresión Lineal: Área Afectada vs Costo Estimado
    # -------------------------------------------------------------
    plt.figure(figsize=(10, 6))
    sns.regplot(
        data=df,
        x='area_m2',
        y='costo_estimado_cop',
        color='#dc2626',
        scatter_kws={'s': 80, 'alpha': 0.8},
        line_kws={'color': '#0f172a', 'linewidth': 2}
    )
    plt.title('Regresión Lineal: Área Afectada (m²) vs Costo de Reparación (COP)', fontsize=14, weight='bold', pad=15)
    plt.xlabel('Área Afectada (m²)', fontsize=12)
    plt.ylabel('Costo Estimado (COP)', fontsize=12)
    plt.tight_layout()
    img3 = os.path.join(ruta_salida, 'pavia_regresion_area_costo.png')
    plt.savefig(img3, dpi=150)
    plt.close()
    print(f"[OK] Gráfico 3 guardado: {img3}")

def preparar_para_ml(df, ruta_salida_csv="data/pavia_preparado_ml.csv"):
    """
    Prepara el DataFrame para algoritmos de Machine Learning:
    1. Codificación ordinal (Label Encoding) para 'prioridad'.
    2. Codificación One-Hot (pd.get_dummies) para 'tipo_dano' y 'barrio'.
    3. Eliminación de identificadores ('id') que no aportan valor predictivo.
    4. Exportación del dataset procesado a CSV.
    """
    print("\n" + "=" * 65)
    print("4. PREPARACIÓN FINAL PARA MACHINE LEARNING (PREPROCESAMIENTO)")
    print("=" * 65)
    
    df_ml = df.copy()
    
    # 1. Codificación Ordinal para 'prioridad' (mantiene la escala de severidad)
    mapeo_prioridad = {'Baja': 1, 'Media': 2, 'Alta': 3, 'Critica': 4}
    df_ml['prioridad_nivel'] = df_ml['prioridad'].map(mapeo_prioridad)
    print("[+] Codificación Ordinal aplicada en 'prioridad' (Baja=1, Media=2, Alta=3, Critica=4).")
    
    # 2. One-Hot Encoding para variables categóricas nominales
    df_ml = pd.get_dummies(
        df_ml,
        columns=['tipo_dano', 'barrio'],
        prefix=['tipo', 'barrio'],
        dtype=int
    )
    print("[+] One-Hot Encoding aplicado en 'tipo_dano' y 'barrio'.")
    
    # 3. Eliminar columnas innecesarias o redundantes para modelado
    columnas_eliminar = ['id', 'prioridad']
    df_ml = df_ml.drop(columns=columnas_eliminar, errors='ignore')
    print(f"[+] Columnas no requeridas para modelado eliminadas: {columnas_eliminar}")
    
    # 4. Guardar archivo preparado
    os.makedirs(os.path.dirname(ruta_salida_csv), exist_ok=True)
    df_ml.to_csv(ruta_salida_csv, index=False)
    print(f"\n[ÉXITO] Dataset preparado para ML guardado en: '{ruta_salida_csv}'")
    print(f"Dimensiones finales: {df_ml.shape[0]} filas x {df_ml.shape[1]} columnas.")
    print("\n--- PRIMERAS 5 FILAS DEL DATASET PARA ML ---")
    print(df_ml.head())
    
    return df_ml

def main():
    print("=" * 65)
    print("PROYECTO PAVIA - PREPARACIÓN DE DATOS Y EDA CON PANDAS Y SEABORN")
    print("=" * 65)
    
    ruta_dataset = os.path.join("data", "deterioro_vial_cartago.csv")
    
    # 1. Cargar datos
    df = cargar_datos(ruta_dataset)
    if df is None:
        return
        
    # 2. Explorar datos con Pandas
    explorar_datos(df)
    
    # 3. Limpieza y Feature Engineering
    df_transformado = limpiar_y_transformar_datos(df)
    
    # 4. Visualizaciones estadísticas avanzadas con Seaborn
    generar_visualizaciones_seaborn(df_transformado)
    
    # 5. Preparar datos para Machine Learning y exportar
    df_ml = preparar_para_ml(df_transformado)
    
    print("\n" + "=" * 65)
    print("PROCESO DE PREPARACIÓN DE DATOS FINALIZADO EXITOSAMENTE")
    print("=" * 65)

if __name__ == "__main__":
    main()
