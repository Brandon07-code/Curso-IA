"""
perceptron_proyecto.py
=============================================================================
PROYECTO: PAVIA (Plataforma Inteligente para la Gestión del Deterioro Vial)
MUNICIPIO: Cartago, Valle del Cauca
ASIGNATURA: Inteligencia Artificial - COTECNOVA (2026-02)
DOCENTE: Jhon James Cano Sánchez
ESTUDIANTES: Brandon Cortes Giraldo & Johan Sttive Linares Barragán
ENTREGABLE: Avance de Proyecto 2 - Segundo Corte
=============================================================================
Modelo: Perceptrón con activación sigmoide, pérdida de entropía cruzada
        binaria y descenso del gradiente implementado desde cero con NumPy.

Objetivo: Predecir si un daño vial requiere intervención prioritaria urgente
          (1 = Alta/Crítica) o rutinaria (0 = Baja/Media) según su superficie
          afectada (area_m2) y el costo estimado de reparación (costo_estimado_cop).
"""

import os
import sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# =============================================================================
# 1. CARGA Y DEFINICIÓN DE VARIABLES DEL PROYECTO
# =============================================================================
# Intentamos buscar el archivo en varias rutas relativas para soportar ejecución
# desde la raíz del proyecto o desde la carpeta src/ (como exige Docker)
posibles_rutas = [
    "data/pavia_preparado_ml.csv",
    "../data/pavia_preparado_ml.csv",
    os.path.join(os.path.dirname(__file__), "..", "data", "pavia_preparado_ml.csv"),
    os.path.join(os.path.dirname(__file__), "data", "pavia_preparado_ml.csv")
]

archivo_datos = None
for r in posibles_rutas:
    if os.path.exists(r):
        archivo_datos = r
        break

if archivo_datos is None:
    print("[ERROR] No se encontró 'pavia_preparado_ml.csv'. Verifique la ruta.")
    sys.exit(1)

df = pd.read_csv(archivo_datos)
print("=" * 70)
print("PAVIA - ENTRENAMIENTO DEL PERCEPTRÓN DESDE CERO (NUMPY)")
print("=" * 70)
print(f"[OK] Dataset cargado: {len(df)} registros viales de Cartago.")

# Variables de entrada numéricas (X):
# x1: area_m2 (superficie del bache/hueco en metros cuadrados)
# x2: costo_estimado_cop (costo de la intervención en pesos colombianos)
X = df[["area_m2", "costo_estimado_cop"]].to_numpy()

# Variable objetivo binaria (y):
# 1 = Intervención urgente (Prioridad Alta o Crítica: prioridad_nivel >= 3)
# 0 = Intervención rutinaria (Prioridad Baja o Media: prioridad_nivel < 3)
y = (df["prioridad_nivel"] >= 3).astype(int).to_numpy()

n_urgentes = np.sum(y == 1)
n_rutinarios = np.sum(y == 0)
print(f"Distribución de clases: {n_urgentes} Daños Urgentes (1) | {n_rutinarios} Daños Rutinarios (0)")
print(f"Dimensiones: X = {X.shape} | y = {y.shape}\n")


# =============================================================================
# 2. DEFINICIÓN DE COMPONENTES DEL PERCEPTRÓN (ÁLGEBRA LINEAL)
# =============================================================================
def suma_ponderada(X, w, b):
    """Calcula el potencial de activación lineal z = X · w + b de forma vectorizada."""
    return np.dot(X, w) + b

def sigmoide(z):
    """Función de activación logística: mapea cualquier z a probabilidad en (0, 1)."""
    return 1.0 / (1.0 + np.exp(-z))

def predecir_probabilidad(X, w, b):
    """Propagación hacia adelante: entrega la probabilidad estimada y_hat."""
    return sigmoide(suma_ponderada(X, w, b))

def calcular_perdida(y_real, y_prob):
    """Entropía cruzada binaria (Log Loss) con recorte numérico para evitar log(0)."""
    epsilon = 1e-9
    y_prob = np.clip(y_prob, epsilon, 1.0 - epsilon)
    return -np.mean(y_real * np.log(y_prob) + (1.0 - y_real) * np.log(1.0 - y_prob))

def calcular_exactitud(y_real, y_prob, umbral=0.5):
    """Porcentaje de clasificaciones acertadas con umbral de decisión."""
    predicciones = (y_prob >= umbral).astype(int)
    return np.mean(predicciones == y_real)

def calcular_gradientes(X, y_real, y_prob):
    """Derivadas analíticas de la pérdida respecto a w y b."""
    n = len(y_real)
    error = y_prob - y_real
    grad_w = np.dot(X.T, error) / n
    grad_b = np.mean(error)
    return grad_w, grad_b


# =============================================================================
# 3. ESTANDARIZACIÓN DE CARACTERÍSTICAS (Z-SCORE)
# =============================================================================
# Las áreas van de 0.2 a 6.5 m² y los costos van de $20,000 a $1,100,000 COP.
# Estandarizamos para evitar explosión de gradientes y desbordamiento en exp(-z).
media = X.mean(axis=0)
desviacion = X.std(axis=0)
X_esc = (X - media) / desviacion

print("[OK] Estandarización Z-Score aplicada correctamente:")
print(f"     Área m²: media={media[0]:.2f}, desv={desviacion[0]:.2f}")
print(f"     Costo COP: media=${media[1]:,.0f}, desv=${desviacion[1]:,.0f}\n")


# =============================================================================
# 4. CICLO DE ENTRENAMIENTO POR DESCENSO DEL GRADIENTE
# =============================================================================
# Inicialización de pesos y sesgo en ceros
w = np.zeros(2)
b = 0.0
tasa_aprendizaje = 0.1
epocas = 500

historial_perdida = []
historial_exactitud = []

print("--- INICIANDO ENTRENAMIENTO (500 ÉPOCAS | lr = 0.1) ---")
for epoca in range(1, epocas + 1):
    # Paso 1: Predicción de probabilidades hacia adelante
    y_prob = predecir_probabilidad(X_esc, w, b)
    
    # Paso 2: Cálculo analítico de gradientes
    grad_w, grad_b = calcular_gradientes(X_esc, y, y_prob)
    
    # Paso 3: Actualización de pesos en sentido contrario al gradiente
    w = w - tasa_aprendizaje * grad_w
    b = b - tasa_aprendizaje * grad_b
    
    # Métricas de control
    perdida_actual = calcular_perdida(y, y_prob)
    exactitud_actual = calcular_exactitud(y, y_prob)
    historial_perdida.append(perdida_actual)
    historial_exactitud.append(exactitud_actual)
    
    if epoca == 1 or epoca % 100 == 0:
        print(f"Época {epoca:>3} | Pérdida: {perdida_actual:.4f} | "
              f"Exactitud: {exactitud_actual:.2%} | w=[{w[0]:.3f}, {w[1]:.3f}] b={b:.3f}")

y_prob_final = predecir_probabilidad(X_esc, w, b)
exactitud_final = calcular_exactitud(y, y_prob_final)
perdida_final = calcular_perdida(y, y_prob_final)

print("\n" + "=" * 70)
print(f"RESULTADO FINAL: Pérdida: {perdida_final:.4f} | Exactitud: {exactitud_final:.2%}")
print(f"Parámetros aprendidos: w1 (área)={w[0]:.4f}, w2 (costo)={w[1]:.4f}, sesgo (b)={b:.4f}")
print("=" * 70)


# =============================================================================
# 5. GENERACIÓN Y GUARDADO DE GRÁFICAS DEL MODELO
# =============================================================================
# Gráfica 1: Curva de Aprendizaje (Pérdida y Exactitud por Época)
fig, (eje1, eje2) = plt.subplots(1, 2, figsize=(12, 4.5))

eje1.plot(historial_perdida, color="#dc2626", linewidth=2)
eje1.set_title("Curva de Pérdida por Época (Binary Cross-Entropy)", fontsize=11, fontweight="bold")
eje1.set_xlabel("Época")
eje1.set_ylabel("Pérdida (Loss)")
eje1.grid(True, alpha=0.3)

eje2.plot(historial_exactitud, color="#16a34a", linewidth=2)
eje2.set_title("Evolución de la Exactitud por Época", fontsize=11, fontweight="bold")
eje2.set_xlabel("Época")
eje2.set_ylabel("Exactitud (Accuracy)")
eje2.set_ylim(0, 1.05)
eje2.grid(True, alpha=0.3)

plt.tight_layout()
ruta_curva = "curva_aprendizaje_pavia.png"
plt.savefig(ruta_curva, dpi=150)
plt.close()
print(f"\n[OK] Gráfico 1 guardado: {ruta_curva}")

# Gráfica 2: Frontera de Decisión Lineal
# Despeje de la recta donde P=0.5 -> w1*x1_esc + w2*x2_esc + b = 0
# x2_esc = -(w1*x1_esc + b) / w2
x1_rango = np.linspace(X[:, 0].min(), X[:, 0].max(), 100)
x1_esc = (x1_rango - media[0]) / desviacion[0]
x2_esc = -(w[0] * x1_esc + b) / w[1]
x2_frontera = x2_esc * desviacion[1] + media[1]

plt.figure(figsize=(9, 6))
plt.scatter(
    X[y == 1, 0], X[y == 1, 1],
    color="#dc2626", edgecolors="black", s=65, label="Intervención Urgente (1)"
)
plt.scatter(
    X[y == 0, 0], X[y == 0, 1],
    color="#2563eb", marker="s", edgecolors="black", s=55, label="Intervención Rutinaria (0)"
)
plt.plot(x1_rango, x2_frontera, color="#0f172a", linewidth=2.5, linestyle="--", label="Frontera de decisión (P = 0.5)")

plt.title("Frontera de Decisión del Perceptrón – Daños Viales en Cartago", fontsize=13, fontweight="bold")
plt.xlabel("Superficie del Daño - Área (m²)", fontsize=11)
plt.ylabel("Costo Estimado de Reparación (COP)", fontsize=11)
plt.ylim(X[:, 1].min() - 20000, X[:, 1].max() + 50000)
plt.legend(frameon=True, facecolor="white", framealpha=0.9)
plt.grid(True, alpha=0.3)
plt.tight_layout()

ruta_frontera = "frontera_decision_pavia.png"
plt.savefig(ruta_frontera, dpi=150)
plt.close()
print(f"[OK] Gráfico 2 guardado: {ruta_frontera}")


# =============================================================================
# 6. EVALUACIÓN Y PREDICCIÓN EN CASOS NUEVOS DE CARTAGO
# =============================================================================
# Definimos 3 reportes reales de ciudadanos en Cartago:
# Caso A: Bache grande en vía principal de Zaragoza (Área 4.5 m², Costo $650,000 COP)
# Caso B: Fisura menor en barrio residencial Álamos (Área 0.6 m², Costo $85,000 COP)
# Caso C: Hueco mediano en zona comercial Centro (Área 2.2 m², Costo $310,000 COP)
casos_nuevos = np.array([
    [4.5, 650000.0],
    [0.6, 85000.0],
    [2.2, 310000.0]
])

casos_nuevos_esc = (casos_nuevos - media) / desviacion
probabilidades = predecir_probabilidad(casos_nuevos_esc, w, b)

print("\n" + "=" * 70)
print("PREDICCIONES DEL PERCEPTRÓN EN REPORTES NUEVOS DE CARTAGO")
print("=" * 70)
nombres_casos = [
    "Reporte 1 (Vía principal Zaragoza - Bache extenso):",
    "Reporte 2 (Calle residencial Álamos - Fisura menor):",
    "Reporte 3 (Zona comercial Centro - Hueco intermedio):"
]

for nombre, (area, costo), prob in zip(nombres_casos, casos_nuevos, probabilidades):
    decision = "URGENTE / PRIORITARIA (1)" if prob >= 0.5 else "RUTINARIA / PROGRAMABLE (0)"
    print(f"{nombre}")
    print(f"   Área: {area:.1f} m² | Costo: ${costo:,.0f} COP -> Probabilidad: {prob:.2%} -> Decisión: {decision}")

print("\n" + "=" * 70)
print("INTERPRETACIÓN DE LOS PESOS PARA LA GESTIÓN VIAL DE CARTAGO:")
print(f" • w1 (Área m²) = {w[0]:+.4f} (Positivo): Mayor tamaño del daño incrementa fuertemente")
print("   la urgencia de bacheo para evitar riesgos y accidentes a motociclistas.")
print(f" • w2 (Costo COP) = {w[1]:+.4f} (Positivo): Daños de mayor costo involucran mayor afectación")
print("   estructural y requieren priorización presupuestal inmediata.")
print(f" • Magnitud relativa: |w1|={abs(w[0]):.2f} vs |w2|={abs(w[1]):.2f}. Ambas variables aportan")
print("   de forma equilibrada y complementaria a la clasificación vial.")
print("=" * 70)
print("\n*** Ejecución completada exitosamente dentro del entorno del proyecto. ***")
