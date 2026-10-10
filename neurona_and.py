"""
neurona_and.py
Implementación de una neurona artificial (Perceptrón simple de Rosenblatt) en Python puro
para aprender la compuerta lógica AND, adaptada a la lógica de decisión vial de PAVIA.

Proyecto: PAVIA (Plataforma Inteligente para la Gestión del Deterioro Vial en Cartago)
Asignatura: Inteligencia Artificial - COTECNOVA
Docente: Jhon James Cano Sánchez
Estudiantes: Brandon Cortes Giraldo & Johan Sttive Linares Barragán

Contexto PAVIA:
Regla de Despacho Inmediato de Cuadrilla (Compuerta AND):
- Entrada x1: ¿El daño tiene gravedad crítica (>= 8)? (1: Sí, 0: No)
- Entrada x2: ¿El daño está ubicado en una vía arterial principal de Cartago? (1: Sí, 0: No)
- Salida esperada y: ¿Se despacha cuadrilla de emergencia inmediata? (1: Solo si x1=1 Y x2=1)
"""

def escalon(z):
    """Función de activación escalón (Heaviside step function)."""
    return 1 if z >= 0 else 0

def neurona(x1, x2, w1, w2, b):
    """Calcula la suma ponderada z y evalúa la activación."""
    z = w1 * x1 + w2 * x2 + b
    return escalon(z)

# Datos de entrenamiento adaptados a la regla AND de PAVIA
# Cada tupla representa: (x1_gravedad_critica, x2_via_arterial, y_despacho_urgente)
datos_and_pavia = [
    (0, 0, 0),  # Daño leve en calle secundaria -> No despacho urgente
    (0, 1, 0),  # Daño leve en vía principal -> No despacho urgente
    (1, 0, 0),  # Daño grave en calle residencial -> Atención programada (no urgente)
    (1, 1, 1),  # Daño grave en vía principal (ej. San Nicolás/Zaragoza) -> DESPACHO URGENTE
]

def entrenar_neurona_and():
    print("=" * 70)
    print("PAVIA - ENTRENAMIENTO DE NEURONA PARA COMPUERTA AND (PYTHON PURO)")
    print("Regla: Despacho Inmediato de Cuadrilla = Gravedad Crítica AND Vía Principal")
    print("=" * 70)

    # Parámetros iniciales
    w1 = 0.1
    w2 = 0.1
    b = 0.0
    tasa_aprendizaje = 0.1
    max_epocas = 15

    print(f"Parámetros iniciales: w1={w1:.3f}, w2={w2:.3f}, b={b:.3f}")
    print(f"Tasa de aprendizaje (alfa): {tasa_aprendizaje}\n")

    errores_por_epoca = []

    for epoca in range(max_epocas):
        error_total = 0
        print(f"--- Época {epoca + 1} ---")
        
        for x1, x2, y_real in datos_and_pavia:
            # 1. Predicción
            y_pred = neurona(x1, x2, w1, w2, b)
            
            # 2. Cálculo del error
            error = y_real - y_pred
            error_total += abs(error)
            
            # 3. Regla de aprendizaje del Perceptrón (ajuste de pesos y bias)
            w1 += tasa_aprendizaje * error * x1
            w2 += tasa_aprendizaje * error * x2
            b += tasa_aprendizaje * error
            
            desc = "Urgente" if y_real == 1 else "No urgente"
            print(f"  Entrada ({x1}, {x2}) [{desc:10s}] | Real: {y_real} | Pred: {y_pred} | Error: {error:2d}")
        
        errores_por_epoca.append(error_total)
        print(f"  -> Error acumulado en la época: {error_total}")
        print(f"  -> Parámetros actualizados: w1={w1:.3f}, w2={w2:.3f}, b={b:.3f}\n")
        
        if error_total == 0:
            print(f"[CONVERGENCIA] La neurona aprendió la regla AND de PAVIA en {epoca + 1} épocas.\n")
            break

    # ============================================================
    # Verificación y prueba final
    # ============================================================
    print("=" * 70)
    print("PRUEBA FINAL DE VALIDACIÓN - REGLA AND EN CARTAGO")
    print("=" * 70)
    casos = [
        ("Calle local, daño leve", 0, 0),
        ("Vía principal, daño leve", 0, 1),
        ("Calle local, daño crítico", 1, 0),
        ("Vía principal (Zaragoza/San Nicolás), daño crítico", 1, 1),
    ]
    for desc, x1, x2 in casos:
        y_pred = neurona(x1, x2, w1, w2, b)
        accion = "DESPACHO INMEDIATO DE CUADRILLA" if y_pred == 1 else "Atención en ruta ordinaria"
        print(f" Caso: {desc}")
        print(f" -> Entradas: (x1={x1}, x2={x2}) | Decisión Neurona: {y_pred} ({accion})\n")

    return errores_por_epoca, (w1, w2, b)

if __name__ == "__main__":
    entrenar_neurona_and()
