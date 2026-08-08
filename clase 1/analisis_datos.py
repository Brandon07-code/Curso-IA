# Análisis de temperaturas en Cartago, Valle del Cauca
# Brandon Cortes Giraldo - Johan Sttive Linares Barragán
# Inteligencia Artificial - COTECNOVA - 2026

# Datos de temperatura semanal en Cartago (grados Celsius)
temperaturas = [32, 35, 28, 38, 41, 30, 36]
dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
ciudad = "Cartago"

print(f"Análisis de temperaturas en {ciudad}, Valle del Cauca")
print("=" * 50)

# Ciclo para recorrer las temperaturas de la semana
for i in range(len(dias)):
    dia = dias[i]
    temp = temperaturas[i]

    if temp > 35:
        estado = "[ALERTA] Calor extremo"
    elif temp > 30:
        estado = "[CUIDADO] Caluroso"
    else:
        estado = "[OK] Agradable"

    print(f"{dia}: {temp} C  -->  {estado}")

# Cálculo de estadísticas básicas
promedio = sum(temperaturas) / len(temperaturas)
maxima = max(temperaturas)
minima = min(temperaturas)

print("=" * 50)
print(f"Temperatura promedio: {promedio:.1f} C")
print(f"Temperatura máxima:   {maxima} C")
print(f"Temperatura mínima:   {minima} C")
