import numpy as np
import pandas as pd

df = pd.read_csv('/mnt/c/Users/Brandon/Desktop/CursoIA/clase9/data/cultivos_cartago.csv')
X = df[['precipitacion_mm', 'temperatura_c']].to_numpy().astype(float)
y = df['cosecha_exitosa'].to_numpy()

def sigmoide(z):
    return 1.0 / (1.0 + np.exp(-z))

def calcular_perdida(y_real, y_prob):
    eps = 1e-9
    y_prob = np.clip(y_prob, eps, 1 - eps)
    return -np.mean(y_real * np.log(y_prob) + (1 - y_real) * np.log(1 - y_prob))

w = np.zeros(2)
b = 0.0
tasa_aprendizaje = 0.1
epocas = 500

for epoca in range(1, epocas + 1):
    z = np.dot(X, w) + b
    y_prob = sigmoide(z)
    error = y_prob - y_real if 'y_real' in locals() else y_prob - y
    gw = np.dot(X.T, error) / len(y)
    gb = np.mean(error)
    w = w - tasa_aprendizaje * gw
    b = b - tasa_aprendizaje * gb

y_prob_final = sigmoide(np.dot(X, w) + b)
exactitud = np.mean((y_prob_final >= 0.5).astype(int) == y)
perdida = calcular_perdida(y, y_prob_final)

print(f"ANTES DEL RETO 5: Perdida: {perdida:.4f} | Exactitud: {exactitud:.2%} | w: [{w[0]:.4f}, {w[1]:.4f}] | b: {b:.4f}")
