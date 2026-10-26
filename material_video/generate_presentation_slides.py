import os
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from PIL import Image

output_dir = "/app/material_video/slides"
os.makedirs(output_dir, exist_ok=True)
cursoia_dir = "/app"

plt.rcParams['font.sans-serif'] = 'DejaVu Sans'
plt.rcParams['font.family'] = 'sans-serif'

# -----------------------------------------------------------------------------
# SLIDE 1: PORTADA
# -----------------------------------------------------------------------------
fig, ax = plt.subplots(figsize=(16, 9), dpi=120)
fig.patch.set_facecolor('#0b1329')
ax.set_facecolor('#0b1329')
ax.set_xlim(0, 16)
ax.set_ylim(0, 9)
ax.axis('off')

ax.text(8, 8.2, "CORPORACIÓN DE ESTUDIOS TECNOLÓGICOS DEL NORTE DEL VALLE (COTECNOVA)", 
        color="#38bdf8", fontsize=15, weight='bold', ha='center')
ax.text(8, 7.7, "FACULTAD DE INGENIERÍA – TECNOLOGÍA EN SISTEMAS / VI SEMESTRE | INTELIGENCIA ARTIFICIAL", 
        color="#94a3b8", fontsize=12, ha='center')

rect_title = patches.FancyBboxPatch((1.5, 4.8), 13, 2.5, boxstyle="round,pad=0.3", 
                                    facecolor="#1e293b", edgecolor="#38bdf8", linewidth=2)
ax.add_patch(rect_title)

ax.text(8, 6.4, "PROYECTO PAVIA", color="#f8fafc", fontsize=34, weight='bold', ha='center')
ax.text(8, 5.7, "Plataforma Inteligente para la Gestión y Priorización del Deterioro Vial en Cartago", 
        color="#38bdf8", fontsize=17, weight='bold', ha='center')
ax.text(8, 5.1, "Sustentación de Avance 2 – Segundo Corte (2026-02)", 
        color="#cbd5e1", fontsize=14, ha='center')

card1 = patches.FancyBboxPatch((1.5, 1.2), 6.2, 3.2, boxstyle="round,pad=0.2", 
                               facecolor="#1e293b", edgecolor="#475569", linewidth=1.5)
ax.add_patch(card1)
ax.text(1.8, 3.9, "Problemática Urbana en Cartago", color="#f59e0b", fontsize=14, weight='bold')
ax.text(1.8, 3.4, "• Proliferación severa de baches, huecos profundos y\n  hundimientos en vías principales y secundarias.", 
        color="#e2e8f0", fontsize=11, linespacing=1.3)
ax.text(1.8, 2.5, "• Alto riesgo de accidentalidad: los motociclistas son\n  quienes más sufren por caídas e impactos viales.", 
        color="#e2e8f0", fontsize=11, linespacing=1.3)
ax.text(1.8, 1.6, "• Gestión pública reactiva: falta de herramientas técnicas\n  para priorizar cuadrillas de bacheo objetivamente.", 
        color="#e2e8f0", fontsize=11, linespacing=1.3)

card2 = patches.FancyBboxPatch((8.3, 1.2), 6.2, 3.2, boxstyle="round,pad=0.2", 
                               facecolor="#1e293b", edgecolor="#475569", linewidth=1.5)
ax.add_patch(card2)
ax.text(8.6, 3.9, "Equipo de Trabajo & Tutoría", color="#10b981", fontsize=14, weight='bold')
ax.text(8.6, 3.3, "• Brandon Cortes Giraldo\n• Johan Sttive Linares Barragán", 
        color="#f8fafc", fontsize=13, weight='bold', linespacing=1.4)
ax.text(8.6, 2.2, "Docente Titular:\n• Jhon James Cano Sánchez", 
        color="#cbd5e1", fontsize=12, linespacing=1.3)
ax.text(8.6, 1.4, "Cartago, Valle del Cauca – Octubre de 2026", 
        color="#94a3b8", fontsize=11)

plt.tight_layout()
s1_path = os.path.join(output_dir, "slide_01_portada.png")
plt.savefig(s1_path, facecolor='#0b1329', dpi=120)
plt.close()

# -----------------------------------------------------------------------------
# SLIDE 2: OBJETIVOS DE ML
# -----------------------------------------------------------------------------
fig, ax = plt.subplots(figsize=(16, 9), dpi=120)
fig.patch.set_facecolor('#0b1329')
ax.set_facecolor('#0b1329')
ax.set_xlim(0, 16)
ax.set_ylim(0, 9)
ax.axis('off')

ax.text(8, 8.2, "PROYECTO PAVIA – AVANCE 2", color="#38bdf8", fontsize=13, weight='bold', ha='center')
ax.text(8, 7.5, "Objetivos de Machine Learning y Modelo Predictivo", color="#f8fafc", fontsize=24, weight='bold', ha='center')

c_width = 4.1
y_card = 1.2
h_card = 5.6

c1 = patches.FancyBboxPatch((1.3, y_card), c_width, h_card, boxstyle="round,pad=0.25", 
                            facecolor="#1e293b", edgecolor="#38bdf8", linewidth=1.5)
ax.add_patch(c1)
ax.text(1.6, 6.3, "1. Transición Técnica", color="#38bdf8", fontsize=16, weight='bold')
ax.text(1.6, 5.6, "• Paso del análisis exploratorio\n  básico a la preparación formal\n  de datos para Machine Learning.", color="#e2e8f0", fontsize=12, linespacing=1.4)
ax.text(1.6, 4.3, "• Estructuración en tensores\n  y matrices de NumPy para\n  procesamiento vectorizado.", color="#e2e8f0", fontsize=12, linespacing=1.4)
ax.text(1.6, 3.0, "• Acondicionamiento numérico\n  con Z-Score para evitar\n  inestabilidad en gradientes.", color="#e2e8f0", fontsize=12, linespacing=1.4)

c2 = patches.FancyBboxPatch((5.95, y_card), c_width, h_card, boxstyle="round,pad=0.25", 
                            facecolor="#1e293b", edgecolor="#10b981", linewidth=1.5)
ax.add_patch(c2)
ax.text(6.25, 6.3, "2. Perceptrón desde Cero", color="#10b981", fontsize=16, weight='bold')
ax.text(6.25, 5.6, "• Algoritmo matemático puro\n  construido con NumPy, sin\n  depender de Scikit-Learn.", color="#e2e8f0", fontsize=12, linespacing=1.4)
ax.text(6.25, 4.3, "• Activación Sigmoide:\n  estimación de probabilidades\n  continuas en el rango (0, 1).", color="#e2e8f0", fontsize=12, linespacing=1.4)
ax.text(6.25, 3.0, "• Descenso del gradiente con\n  Entropía Cruzada Binaria\n  para convergencia óptima.", color="#e2e8f0", fontsize=12, linespacing=1.4)

c3 = patches.FancyBboxPatch((10.6, y_card), c_width, h_card, boxstyle="round,pad=0.25", 
                            facecolor="#1e293b", edgecolor="#f59e0b", linewidth=1.5)
ax.add_patch(c3)
ax.text(10.9, 6.3, "3. Impacto en Cartago", color="#f59e0b", fontsize=16, weight='bold')
ax.text(10.9, 5.6, "• Clasificación automática de\n  daños viales en dos clases:\n  Urgente (1) vs Rutinario (0).", color="#e2e8f0", fontsize=12, linespacing=1.4)
ax.text(10.9, 4.3, "• Priorización inteligente basada\n  en severidad física y costo\n  estimado de reparación.", color="#e2e8f0", fontsize=12, linespacing=1.4)
ax.text(10.9, 3.0, "• Soporte técnico objetivo a la\n  Alcaldía y Secretaría de\n  Infraestructura de Cartago.", color="#e2e8f0", fontsize=12, linespacing=1.4)

plt.tight_layout()
s2_path = os.path.join(output_dir, "slide_02_objetivos.png")
plt.savefig(s2_path, facecolor='#0b1329', dpi=120)
plt.close()

# -----------------------------------------------------------------------------
# SLIDE 3: DATOS Y FEATURE ENGINEERING
# -----------------------------------------------------------------------------
fig, ax = plt.subplots(figsize=(16, 9), dpi=120)
fig.patch.set_facecolor('#0b1329')
ax.set_facecolor('#0b1329')
ax.set_xlim(0, 16)
ax.set_ylim(0, 9)
ax.axis('off')

ax.text(8, 8.2, "PROYECTO PAVIA – AVANCE 2", color="#38bdf8", fontsize=13, weight='bold', ha='center')
ax.text(8, 7.5, "Preparación de Datos y Feature Engineering (Pandas)", color="#f8fafc", fontsize=24, weight='bold', ha='center')

b_left = patches.FancyBboxPatch((1.2, 1.2), 6.5, 5.7, boxstyle="round,pad=0.25", 
                                facecolor="#1e293b", edgecolor="#38bdf8", linewidth=1.5)
ax.add_patch(b_left)
ax.text(1.5, 6.4, "Expansión y Limpieza del Dataset", color="#38bdf8", fontsize=16, weight='bold')
ax.text(1.5, 5.8, "• Ampliación representativa: se escaló de 15 a 120 registros\n  viales representativos en 15 barrios de Cartago.", color="#e2e8f0", fontsize=11, linespacing=1.3)
ax.text(1.5, 5.0, "• Cobertura territorial urbana: Centro, El Prado, Zaragoza,\n  San Jerónimo, La Floresta, Álamos, Bellavista, etc.", color="#e2e8f0", fontsize=11, linespacing=1.3)
ax.text(1.5, 4.2, "• 100% Calidad del dato: verificación rigurosa de 0 nulos\n  y casteo numérico correcto (area_m2 a float, costo a int).", color="#e2e8f0", fontsize=11, linespacing=1.3)

ax.text(1.5, 3.4, "Feature Engineering (Columnas Creadas)", color="#10b981", fontsize=15, weight='bold')
ax.text(1.5, 2.7, "1. costo_por_m2 = costo_estimado_cop / area_m2\n   Normaliza el costo unitario de bacheo por metro cuadrado.", color="#e2e8f0", fontsize=11, linespacing=1.3)
ax.text(1.5, 1.7, "2. indice_criticidad = gravedad * area_m2\n   Ponderación física entre severidad (1-10) y superficie (m²).", color="#e2e8f0", fontsize=11, linespacing=1.3)

b_right = patches.FancyBboxPatch((8.3, 1.2), 6.5, 5.7, boxstyle="round,pad=0.25", 
                                 facecolor="#1e293b", edgecolor="#475569", linewidth=1.5)
ax.add_patch(b_right)
ax.text(8.6, 6.4, "Tabla Comparativa: Antes vs Después", color="#f59e0b", fontsize=16, weight='bold')

table_data = [
    ("Métrica", "Antes (Avance 1)", "Después (Avance 2)"),
    ("Registros (filas)", "15 observaciones", "120 baches reales"),
    ("Dimensiones", "7 columnas básicas", "27 columnas para ML"),
    ("Valores nulos", "0 nulos", "0 nulos (100% limpio)"),
    ("Feature Engineering", "Ninguna", "costo_por_m2, indice_criticidad"),
    ("Codificación", "Texto libre", "Ordinal + One-Hot Encoding")
]

y_pos = 5.7
for i, row in enumerate(table_data):
    is_head = (i == 0)
    bg_color = "#334155" if is_head else ("#1e293b" if i % 2 == 1 else "#0f172a")
    rect = patches.Rectangle((8.6, y_pos - 0.45), 5.9, 0.55, facecolor=bg_color, edgecolor="#475569", linewidth=0.8)
    ax.add_patch(rect)
    
    c_text = "#38bdf8" if is_head else "#f8fafc"
    weight = 'bold' if is_head else 'normal'
    ax.text(8.8, y_pos - 0.25, row[0], color=c_text, fontsize=10.5, weight=weight)
    ax.text(11.0, y_pos - 0.25, row[1], color=c_text, fontsize=10.5, weight=weight)
    ax.text(13.0, y_pos - 0.25, row[2], color=c_text, fontsize=10.5, weight=weight)
    y_pos -= 0.65

ax.text(8.6, 1.5, "Exportación final lista para entrenamiento:\n• Archivo: data/pavia_preparado_ml.csv", color="#38bdf8", fontsize=11, weight='bold')

plt.tight_layout()
s3_path = os.path.join(output_dir, "slide_03_datos_limpieza.png")
plt.savefig(s3_path, facecolor='#0b1329', dpi=120)
plt.close()

# -----------------------------------------------------------------------------
# SLIDE 4: SEABORN (3 Gráficos reales integrados)
# -----------------------------------------------------------------------------
fig, ax = plt.subplots(figsize=(16, 9), dpi=120)
fig.patch.set_facecolor('#0b1329')
ax.set_facecolor('#0b1329')
ax.set_xlim(0, 16)
ax.set_ylim(0, 9)
ax.axis('off')

ax.text(8, 8.4, "PROYECTO PAVIA – AVANCE 2", color="#38bdf8", fontsize=13, weight='bold', ha='center')
ax.text(8, 7.8, "Análisis Visual de Daños Viales con Seaborn", color="#f8fafc", fontsize=23, weight='bold', ha='center')

img1 = Image.open(f"{cursoia_dir}/pavia_distribucion_costo_seaborn.png")
img2 = Image.open(f"{cursoia_dir}/pavia_boxplot_costo_tipo_dano.png")
img3 = Image.open(f"{cursoia_dir}/pavia_regresion_area_costo.png")

ax_i1 = fig.add_axes([0.06, 0.22, 0.28, 0.48])
ax_i1.imshow(img1)
ax_i1.axis('off')

ax_i2 = fig.add_axes([0.36, 0.22, 0.28, 0.48])
ax_i2.imshow(img2)
ax_i2.axis('off')

ax_i3 = fig.add_axes([0.66, 0.22, 0.28, 0.48])
ax_i3.imshow(img3)
ax_i3.axis('off')

box_bot = patches.FancyBboxPatch((0.9, 0.05), 14.2, 1.4, boxstyle="round,pad=0.2", 
                                 facecolor="#1e293b", edgecolor="#38bdf8", linewidth=1.5)
ax.add_patch(box_bot)
ax.text(1.2, 1.15, "Hallazgos Principales del Análisis Exploratorio:", color="#38bdf8", fontsize=12, weight='bold')
ax.text(1.2, 0.75, "1. Distribución: Mayoría de reparaciones entre COP 80.000 y COP 400.000; casos críticos superan COP 1.000.000.", color="#e2e8f0", fontsize=10.5)
ax.text(1.2, 0.45, "2. Tipologías: Huecos profundos y hundimientos generan los mayores costos e impacto vial en Cartago.", color="#e2e8f0", fontsize=10.5)
ax.text(1.2, 0.15, "3. Regresión: Fuerte relación lineal área vs costo -> Justifica usar área y costo como entradas del perceptrón.", color="#e2e8f0", fontsize=10.5)

s4_path = os.path.join(output_dir, "slide_04_seaborn.png")
plt.savefig(s4_path, facecolor='#0b1329', dpi=120)
plt.close()

# -----------------------------------------------------------------------------
# SLIDE 5: PERCEPTRÓN RESULTADOS (Curva y Frontera)
# -----------------------------------------------------------------------------
fig, ax = plt.subplots(figsize=(16, 9), dpi=120)
fig.patch.set_facecolor('#0b1329')
ax.set_facecolor('#0b1329')
ax.set_xlim(0, 16)
ax.set_ylim(0, 9)
ax.axis('off')

ax.text(8, 8.4, "PROYECTO PAVIA – AVANCE 2", color="#38bdf8", fontsize=13, weight='bold', ha='center')
ax.text(8, 7.8, "Resultados del Perceptrón: Curva de Aprendizaje y Frontera de Decisión", color="#f8fafc", fontsize=22, weight='bold', ha='center')

img_curva = Image.open(f"{cursoia_dir}/curva_aprendizaje_pavia.png")
img_front = Image.open(f"{cursoia_dir}/frontera_decision_pavia.png")

ax_c = fig.add_axes([0.05, 0.20, 0.44, 0.52])
ax_c.imshow(img_curva)
ax_c.axis('off')

ax_f = fig.add_axes([0.51, 0.20, 0.44, 0.52])
ax_f.imshow(img_front)
ax_f.axis('off')

box_bot2 = patches.FancyBboxPatch((0.8, 0.04), 14.4, 1.4, boxstyle="round,pad=0.2", 
                                  facecolor="#1e293b", edgecolor="#10b981", linewidth=1.5)
ax.add_patch(box_bot2)
ax.text(1.1, 1.15, "Métricas de Entrenamiento y Predicciones en Cartago:", color="#10b981", fontsize=12, weight='bold')
ax.text(1.1, 0.8, "• Pérdida: reducida de 0.6931 a 0.0893 | Exactitud: 97.50% (117 aciertos de 120 lotes viales).", color="#e2e8f0", fontsize=10.5)
ax.text(1.1, 0.5, "• Pesos aprendidos: w1 (área) = +2.1753 | w2 (costo) = +2.4837 | sesgo (b) = -1.2373.", color="#e2e8f0", fontsize=10.5)
ax.text(1.1, 0.2, "• Casos nuevos: Bache en Zaragoza (4.5 m², COP 650.000) -> 99.70% URGENTE | Álamos (0.6 m², COP 85.000) -> 0.52% RUTINARIO.", color="#e2e8f0", fontsize=10.5)

s5_path = os.path.join(output_dir, "slide_05_perceptron_resultados.png")
plt.savefig(s5_path, facecolor='#0b1329', dpi=120)
plt.close()

# -----------------------------------------------------------------------------
# SLIDE 6: PRÓXIMOS PASOS (TERCER CORTE)
# -----------------------------------------------------------------------------
fig, ax = plt.subplots(figsize=(16, 9), dpi=120)
fig.patch.set_facecolor('#0b1329')
ax.set_facecolor('#0b1329')
ax.set_xlim(0, 16)
ax.set_ylim(0, 9)
ax.axis('off')

ax.text(8, 8.2, "PROYECTO PAVIA – AVANCE 2", color="#38bdf8", fontsize=13, weight='bold', ha='center')
ax.text(8, 7.5, "Próximos Pasos – Hacia el Proyecto Final (Tercer Corte)", color="#f8fafc", fontsize=24, weight='bold', ha='center')

c_left = patches.FancyBboxPatch((1.3, 1.2), 6.5, 5.6, boxstyle="round,pad=0.25", 
                                facecolor="#1e293b", edgecolor="#38bdf8", linewidth=1.5)
ax.add_patch(c_left)
ax.text(1.6, 6.3, "1. Migración a Scikit-Learn", color="#38bdf8", fontsize=17, weight='bold')
ax.text(1.6, 5.5, "• Modelos Supervisados Avanzados:\n  Evaluación y entrenamiento de Random Forest\n  Classifier y Regresión Logística Multiclase.", color="#e2e8f0", fontsize=12, linespacing=1.4)
ax.text(1.6, 4.0, "• Clasificación en 4 Niveles de Prioridad:\n  Superar la barrera binaria para clasificar en:\n  Baja (1), Media (2), Alta (3) y Crítica (4).", color="#e2e8f0", fontsize=12, linespacing=1.4)
ax.text(1.6, 2.5, "• Validación Estadística Completa:\n  Matrices de confusión, curvas ROC-AUC, precisión,\n  recall y F1-Score con validación cruzada.", color="#e2e8f0", fontsize=12, linespacing=1.4)

c_right = patches.FancyBboxPatch((8.2, 1.2), 6.5, 5.6, boxstyle="round,pad=0.25", 
                                 facecolor="#1e293b", edgecolor="#10b981", linewidth=1.5)
ax.add_patch(c_right)
ax.text(8.5, 6.3, "2. Interfaz Gráfica Interactiva", color="#10b981", fontsize=17, weight='bold')
ax.text(8.5, 5.5, "• Mapa Georreferenciado de Cartago:\n  Visualización en tiempo real de los reportes viales\n  con marcadores por severidad y mapa de calor.", color="#e2e8f0", fontsize=12, linespacing=1.4)
ax.text(8.5, 4.0, "• Panel para la Secretaría de Infraestructura:\n  Módulo dinámico para simular costos de bacheo y\n  generar rutas optimizadas para cuadrillas.", color="#e2e8f0", fontsize=12, linespacing=1.4)
ax.text(8.5, 2.5, "• Participación Ciudadana:\n  Formulario intuitivo para que la comunidad reporte\n  daños con ubicación y foto desde su celular.", color="#e2e8f0", fontsize=12, linespacing=1.4)

ax.text(8, 0.5, "¡Muchas gracias por su atención! – Proyecto PAVIA (COTECNOVA)", color="#cbd5e1", fontsize=13, ha='center', weight='bold')

plt.tight_layout()
s6_path = os.path.join(output_dir, "slide_06_proximos_pasos.png")
plt.savefig(s6_path, facecolor='#0b1329', dpi=120)
plt.close()
print("Todas las 6 diapositivas generadas con acentos, tildes y 'ñ' correctas.")
