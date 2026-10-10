"""
neuronas_logicas.py
Implementación de neuronas artificiales (Perceptrón simple) en Python puro
para compuertas lógicas (OR, NOT, AND) y demostración del límite de la compuerta XOR,
adaptadas a las reglas de decisión de la plataforma PAVIA en Cartago.

Proyecto: PAVIA (Plataforma Inteligente para la Gestión del Deterioro Vial en Cartago)
Asignatura: Inteligencia Artificial - COTECNOVA
Docente: Jhon James Cano Sánchez
Estudiantes: Brandon Cortes Giraldo & Johan Sttive Linares Barragán
"""

import os
import matplotlib.pyplot as plt

def escalon(z):
    """Función de activación escalón (Heaviside step function)."""
    return 1 if z >= 0 else 0

# ==============================================================================
# 1. COMPUERTA LÓGICA OR (Regla: Bacheo Preventivo en Cartago)
# Entrada x1: Fisura temprana detectada | Entrada x2: Proximidad temporada de lluvias
# Salida y: 1 si al menos una condición se cumple (Agendar intervención preventiva)
# ==============================================================================
def entrenar_compuerta_or():
    print("=" * 70)
    print("1. ENTRENAMIENTO DE NEURONA PARA COMPUERTA OR (PAVIA)")
    print("Regla: Agendar Bacheo Preventivo = Fisura Detectada OR Temporada Lluvias")
    print("=" * 70)
    
    datos_or = [
        (0, 0, 0),
        (0, 1, 1),
        (1, 0, 1),
        (1, 1, 1)
    ]
    
    w1, w2, b = 0.1, 0.1, -0.2
    alfa = 0.1
    max_epocas = 15
    errores = []
    
    print(f"Parámetros iniciales: w1={w1:.2f}, w2={w2:.2f}, b={b:.2f} | Tasa de aprendizaje: {alfa}")
    
    for epoca in range(max_epocas):
        error_total = 0
        for x1, x2, y_real in datos_or:
            z = w1 * x1 + w2 * x2 + b
            y_pred = escalon(z)
            error = y_real - y_pred
            error_total += abs(error)
            
            # Ajuste de pesos y bias
            w1 += alfa * error * x1
            w2 += alfa * error * x2
            b += alfa * error
            
        errores.append(error_total)
        print(f"Época {epoca + 1:2d} | Error acumulado: {error_total:2d} | w1={w1:.3f}, w2={w2:.3f}, b={b:.3f}")
        if error_total == 0:
            print(f"[CONVERGENCIA] La compuerta OR aprendió en {epoca + 1} épocas.\n")
            break
            
    print("Prueba de validación OR:")
    for x1, x2, y_real in datos_or:
        y_pred = escalon(w1 * x1 + w2 * x2 + b)
        print(f"  Entrada ({x1}, {x2}) -> Esperado: {y_real} | Predicho: {y_pred} [{'OK' if y_pred == y_real else 'FAIL'}]")
    print()
    return errores, (w1, w2, b)

# ==============================================================================
# 2. COMPUERTA LÓGICA NOT (Regla: Transitabilidad Segura de la Calzada)
# Entrada x1: Daño vial reportado en calzada (1: Sí, 0: No)
# Salida y: Calzada 100% segura para motociclistas (1 si no hay daño, 0 si hay daño)
# ==============================================================================
def entrenar_compuerta_not():
    print("=" * 70)
    print("2. ENTRENAMIENTO DE NEURONA PARA COMPUERTA NOT (PAVIA)")
    print("Regla: Calzada Segura = NOT(Deterioro Vial Activo)")
    print("=" * 70)
    
    datos_not = [
        (0, 1), # Vía sin daño -> Calzada Segura (1)
        (1, 0)  # Vía con daño -> Calzada NO Segura (0)
    ]
    
    w1, b = 0.1, 0.1
    alfa = 0.1
    max_epocas = 15
    errores = []
    
    print(f"Parámetros iniciales: w1={w1:.2f}, b={b:.2f} | Tasa de aprendizaje: {alfa}")
    
    for epoca in range(max_epocas):
        error_total = 0
        for x1, y_real in datos_not:
            z = w1 * x1 + b
            y_pred = escalon(z)
            error = y_real - y_pred
            error_total += abs(error)
            
            # Ajuste de peso y bias (1 entrada)
            w1 += alfa * error * x1
            b += alfa * error
            
        errores.append(error_total)
        print(f"Época {epoca + 1:2d} | Error acumulado: {error_total:2d} | w1={w1:.3f}, b={b:.3f}")
        if error_total == 0:
            print(f"[CONVERGENCIA] La compuerta NOT aprendió en {epoca + 1} épocas.\n")
            break
            
    print("Prueba de validación NOT:")
    for x1, y_real in datos_not:
        y_pred = escalon(w1 * x1 + b)
        print(f"  Entrada ({x1}) -> Esperado: {y_real} | Predicho: {y_pred} [{'OK' if y_pred == y_real else 'FAIL'}]")
    print()
    return errores, (w1, b)

# ==============================================================================
# 3. COMPUERTA LÓGICA AND (Regla: Despacho Inmediato de Cuadrilla)
# ==============================================================================
def entrenar_compuerta_and():
    print("=" * 70)
    print("3. ENTRENAMIENTO DE NEURONA PARA COMPUERTA AND (PAVIA)")
    print("=" * 70)
    
    datos_and = [
        (0, 0, 0),
        (0, 1, 0),
        (1, 0, 0),
        (1, 1, 1)
    ]
    
    w1, w2, b = 0.1, 0.1, 0.0
    alfa = 0.1
    max_epocas = 15
    errores = []
    
    for epoca in range(max_epocas):
        error_total = 0
        for x1, x2, y_real in datos_and:
            z = w1 * x1 + w2 * x2 + b
            y_pred = escalon(z)
            error = y_real - y_pred
            error_total += abs(error)
            
            w1 += alfa * error * x1
            w2 += alfa * error * x2
            b += alfa * error
            
        errores.append(error_total)
        if error_total == 0:
            print(f"[CONVERGENCIA] La compuerta AND aprendió en {epoca + 1} épocas.\n")
            break
            
    return errores, (w1, w2, b)

# ==============================================================================
# 4. COMPUERTA LÓGICA XOR (Demostración de No-Separabilidad Lineal)
# ==============================================================================
def entrenar_compuerta_xor():
    print("=" * 70)
    print("4. DEMOSTRACIÓN DE LÍMITE: COMPUERTA XOR (NO SEPARABLE LINEALMENTE)")
    print("=" * 70)
    
    datos_xor = [
        (0, 0, 0),
        (0, 1, 1),
        (1, 0, 1),
        (1, 1, 0)
    ]
    
    w1, w2, b = 0.1, 0.1, 0.0
    alfa = 0.1
    max_epocas = 15
    errores = []
    
    for epoca in range(max_epocas):
        error_total = 0
        for x1, x2, y_real in datos_xor:
            z = w1 * x1 + w2 * x2 + b
            y_pred = escalon(z)
            error = y_real - y_pred
            error_total += abs(error)
            
            w1 += alfa * error * x1
            w2 += alfa * error * x2
            b += alfa * error
            
        errores.append(error_total)
        print(f"Época {epoca + 1:2d} | Error acumulado: {error_total:2d} (El error no baja a 0)")
        
    print("\n[RESULTADO XOR] Un perceptrón simple NO puede converger para XOR.")
    print("Razón teórica: XOR no es linealmente separable con una sola recta de decisión.\n")
    return errores

def graficar_evolucion_errores(err_and, err_or, err_not, err_xor):
    """Genera gráfica comparativa de la evolución del error con Matplotlib."""
    plt.figure(figsize=(11, 7))
    plt.style.use('seaborn-v0_8-whitegrid' if 'seaborn-v0_8-whitegrid' in plt.style.available else 'default')
    
    plt.plot(range(1, len(err_and) + 1), err_and, marker='o', linewidth=2.5, color='#0d9488', label='Compuerta AND (PAVIA)')
    plt.plot(range(1, len(err_or) + 1), err_or, marker='s', linewidth=2.5, color='#2563eb', label='Compuerta OR (PAVIA)')
    plt.plot(range(1, len(err_not) + 1), err_not, marker='^', linewidth=2.5, color='#16a34a', label='Compuerta NOT (PAVIA)')
    plt.plot(range(1, len(err_xor) + 1), err_xor, marker='x', linestyle='--', linewidth=2, color='#dc2626', label='Compuerta XOR (No converge)')
    
    plt.title('Evolución y Disminución del Error por Épocas (Perceptrón Simple - PAVIA)', fontsize=14, weight='bold', pad=15)
    plt.xlabel('Época de Entrenamiento', fontsize=12)
    plt.ylabel('Error Total Acumulado (|y_real - y_pred|)', fontsize=12)
    plt.ylim(-0.5, 4.5)
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.legend(fontsize=11, frameon=True)
    plt.tight_layout()
    
    ruta_img = 'evolucion_error_compuertas.png'
    plt.savefig(ruta_img, dpi=150)
    plt.close()
    print(f"[IMAGEN GENERADA] Gráfica guardada exitosamente: '{ruta_img}'")

def main():
    err_and, params_and = entrenar_compuerta_and()
    err_or, params_or = entrenar_compuerta_or()
    err_not, params_not = entrenar_compuerta_not()
    err_xor = entrenar_compuerta_xor()
    
    graficar_evolucion_errores(err_and, err_or, err_not, err_xor)

if __name__ == "__main__":
    main()
