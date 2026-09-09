# PAVIA - Plataforma Inteligente de Gestión del Deterioro Vial

**Asignatura:** Inteligencia Artificial (Semestre VI)  
**Institución:** COTECNOVA — Tecnología en Gestión de Sistemas de Información  
**Estudiantes:** Brandon Cortes Giraldo — Johan Sttive Linares Barragán  
**Ciudad:** Cartago, Valle del Cauca — Colombia (2026)  

---

## 1. Descripción del Proyecto
**PAVIA** es una plataforma basada en Inteligencia Artificial y Visión por Computadora diseñada para la detección, clasificación y análisis del deterioro vial en el municipio de Cartago, Valle del Cauca. El sistema permite a la administración municipal y a los ciudadanos reportar daños, priorizar cuadrillas de reparación y evaluar riesgos vehiculares en tiempo real.

---

## 2. Análisis Exploratorio de Datos (EDA) con NumPy y Matplotlib

Como parte del avance de desarrollo del primer corte, se procesó el dataset de 15 reportes viales georreferenciados en barrios representativos de Cartago (`data/deterioro_vial_cartago.csv`).

### A. Variables Analizadas
* **`gravedad`:** Nivel de severidad estructural del daño (escala de 1 a 10).
* **`area_m2`:** Superficie física afectada en metros cuadrados.
* **`costo_estimado_cop`:** Presupuesto estimado en pesos colombianos para el bacheo o pavimentación.

### B. Estadísticas Descriptivas (Calculadas con NumPy)

| Variable | Media | Mediana | Desv. Estándar | Mínimo | Máximo |
|---|---|---|---|---|---|
| **Gravedad (1 - 10)** | 6.47 | 7.00 | 2.42 | 2.00 | 10.00 |
| **Área Afectada (m²)** | 2.33 m² | 2.50 m² | 1.35 m² | 0.40 m² | 4.80 m² |
| **Costo Reparación (COP)** | $308,666.67 | $350,000.00 | $165,080.45 | $80,000.00 | $600,000.00 |
| **Costo Total Dataset** | **$4,630,000.00 COP** | — | — | — | — |

### C. Visualizaciones Generadas con Matplotlib
* `pavia_costo_por_barrio.png`: Gráfico de barras comparando el presupuesto de intervención necesario por barrio en Cartago (destacando barrios críticos como San Nicolás, Zaragoza y Jorge Eliécer Gaitán).
* `pavia_area_vs_costo.png`: Gráfico de dispersión demostrando una correlación positiva directa entre el tamaño del daño ($m^2$) y el costo en materiales.
* `pavia_distribucion_gravedad.png`: Histograma que evidencia una concentración de reportes en niveles de severidad alta ($\ge 8/10$).

### D. Influencia en el Futuro Modelo de IA
1. **Reglas de Priorización:** Los daños clasificados con severidad $\ge 8$ y costo $> \$400,000$ COP se etiquetan automáticamente como *Prioridad Crítica* para la asignación inmediata de cuadrillas.
2. **Entrenamiento de Visión por Computadora (YOLOv8):** La correlación entre área y tipo de daño servirá para alimentar el modelo de visión que estimará la severidad a partir de fotografías tomadas por los ciudadanos.

---

## 3. Tecnologías
- Python 3.12
- Docker & Docker Compose
- NumPy, Matplotlib, Pandas, Scikit-Learn
- Git & GitHub

## 4. Ejecución del Entorno

### Ejecutar el análisis EDA:
```bash
python eda_proyecto.py
```

### Ejecutar con Docker:
```bash
docker compose up -d
docker exec python_ia python eda_proyecto.py
```
