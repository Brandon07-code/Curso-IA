import numpy as np
import pandas as pd

df = pd.read_csv('/mnt/c/Users/Brandon/Desktop/CursoIA/clase9/data/cultivos_cartago.csv')
X = df[['precipitacion_mm', 'temperatura_c']].to_numpy().astype(float)
y = df['cosecha_exitosa'].to_numpy()

media = X.mean(axis=0)
desviacion = X.std(axis=0)
X_esc = (X - media) / desviacion

def sigmoide(z): return 1.0 / (1.0 + np.exp(-z))
def calcular_perdida(y_real, y_prob):
    eps = 1e-9; y_prob = np.clip(y_prob, eps, 1-eps)
    return -np.mean(y_real * np.log(y_prob) + (1-y_real) * np.log(1-y_prob))

def entrenar(lr, epocas):
    w = np.zeros(2)
    b = 0.0
    for _ in range(epocas):
        p = sigmoide(np.dot(X_esc, w) + b)
        err = p - y
        gw = np.dot(X_esc.T, err) / len(y)
        gb = np.mean(err)
        w -= lr * gw
        b -= lr * gb
    p_final = sigmoide(np.dot(X_esc, w) + b)
    acc = np.mean((p_final >= 0.5).astype(int) == y)
    loss = calcular_perdida(y, p_final)
    return loss, acc, w, b

print("--- EXPERIMENTO A: TASA DE APRENDIZAJE ---")
for lr in [0.001, 0.1, 1.0]:
    loss, acc, w, b = entrenar(lr, 500)
    print(f"lr={lr:<5} | Perdida: {loss:.4f} | Exactitud: {acc:.2%} | w=[{w[0]:.3f}, {w[1]:.3f}] b={b:.3f}")

print("\n--- EXPERIMENTO B: NUMERO DE EPOCAS ---")
for ep in [20, 500, 3000]:
    loss, acc, w, b = entrenar(0.1, ep)
    print(f"epocas={ep:<4} | Perdida: {loss:.4f} | Exactitud: {acc:.2%} | w=[{w[0]:.3f}, {w[1]:.3f}] b={b:.3f}")
