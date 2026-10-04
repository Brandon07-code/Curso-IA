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

---

## 3. Preparación de Datos para Machine Learning (Pandas & Seaborn)

En concordancia con los requerimientos de la Clase 7/8, se desarrolló el pipeline de preparación de datos en `preparacion_datos_pavia.py`, transformando los datos crudos en un dataset codificado para Machine Learning (`data/pavia_preparado_ml.csv`).

### A. Diagnóstico y Manejo de Valores Nulos
* Mediante `df.isnull().sum()` se constató que el dataset inicial presenta un **100% de completitud** en sus 15 registros.
* Se configuró lógica preventiva en el script para que, ante cualquier dato faltante en variables numéricas (`gravedad`, `area_m2`, `costo_estimado_cop`), se aplique imputación con la **mediana**, evitando distorsiones por valores atípicos.

### B. Creación de Columnas Derivadas (Feature Engineering)
Se incorporaron dos métricas matemáticas calculadas directamente con Pandas:
1. **`costo_por_m2`:** $\frac{\text{costo\_estimado\_cop}}{\text{area\_m2}}$, que cuantifica el costo unitario por metro cuadrado para evaluar la eficiencia del gasto público.
2. **`indice_criticidad`:** $\text{gravedad} \times \text{area\_m2}$, que combina la severidad estructural (1 a 10) con la superficie física afectada, ofreciendo una métrica objetiva para el despacho de cuadrillas de obras públicas.

### C. Codificación de Variables Categóricas
* **Codificación Ordinal:** Para la variable `prioridad` se aplicó un mapeo jerárquico (`Baja=1, Media=2, Alta=3, Critica=4`), manteniendo la relación de orden para algoritmos de clasificación.
* **One-Hot Encoding (`pd.get_dummies`):** Para las variables nominales `tipo_dano` y `barrio` se crearon columnas binarias (0 y 1), impidiendo que los algoritmos de IA asuman un orden numérico arbitrario entre sectores o fallas.
* **Selección de Características:** Se eliminó la columna `id` por carecer de poder predictivo, obteniendo una matriz final de **15 filas y 27 columnas numéricas** lista para Scikit-Learn.

### D. Visualizaciones Estadísticas Avanzadas con Seaborn
* **`pavia_distribucion_costo_seaborn.png`:** Histograma con curva de densidad KDE que evidencia una distribución bimodal, con picos en intervenciones menores (~$150.000 COP) y reparaciones estructurales mayores (~$450.000 COP).
* **`pavia_boxplot_costo_tipo_dano.png`:** Diagrama de caja que constata que los *Huecos profundos* y *Hundimientos* concentran la mayor mediana y variabilidad de costos, mientras que las *Fisuras* son homogéneas y de bajo impacto.
* **`pavia_regresion_area_costo.png`:** Gráfico con línea de regresión lineal confirmando una relación lineal directa y positiva ($R^2$ elevado) entre la superficie dañada y el costo presupuestal.

### E. Respuestas al Cuestionario de Interpretación (Sección 6.4 de la Clase)
1. **Exploración de Datos:**
   * **Dimensiones:** El dataset original contiene **15 filas y 7 columnas**. Tras el preprocesamiento y codificación One-Hot, se expande a **15 filas y 27 columnas numéricas**.
   * **Tipos de datos:** Originalmente `int64` (`id`, `gravedad`, `costo_estimado_cop`), `float64` (`area_m2`) y `object` (`barrio`, `tipo_dano`, `prioridad`).
   * **Valores nulos:** Se verificó con `df.isnull().sum()`, arrojando un conteo de 0 en todas las columnas (100% de integridad estructural).

2. **Limpieza y Manejo de Nulos:**
   * **Estrategia:** Se programó lógica defensiva mediante imputación con la **mediana** para variables cuantitativas continuas en caso de reportes incompletos.
   * **¿Por qué la mediana y no la media?:** Porque la media aritmética es sumamente susceptible a ser distorsionada por valores extremos o atípicos (*outliers*), mientras que la mediana refleja con precisión el valor central del 50% de la población sin sesgos.

3. **Visualización e Interpretación:**
   * **Categoría con mayor costo:** La tipología de **Hueco profundo** y **Hundimiento** en sectores arteriales como San Nicolás y Zaragoza concentran los presupuestos individuales más elevados, superando los $500.000 y $600.000 COP por daño.
   * **Relación entre variables:** El gráfico de dispersión con recta de regresión (`sns.regplot`) evidencia una correlación lineal positiva muy fuerte: a mayor superficie afectada en $m^2$, el costo en mezcla asfáltica y horas de cuadrilla se incrementa de forma directamente proporcional.

4. **Preparación para Machine Learning:**
   * **Columnas codificadas:** Se aplicó One-Hot Encoding binario sobre `tipo_dano` y `barrio` (variables nominales) y codificación ordinal entera sobre `prioridad` (Baja=1, Media=2, Alta=3, Crítica=4).
   * **¿Por qué se eliminaron identificadores y texto libre?:** Se eliminó la columna `id` porque es un identificador artificial sin correlación con la física del daño vial; conservarla provocaría que el modelo aprenda a memorizar registros (*data leakage* / sobreajuste) en lugar de generalizar patrones reales.

5. **Propuesta de Optimización del Código:**
   * Se propone encapsular todo el flujo de preprocesamiento dentro de un `Pipeline` o `ColumnTransformer` de **Scikit-Learn**. Esto automatizará la imputación (`SimpleImputer`), el escalado numérico (`StandardScaler`) y la codificación categórica (`OneHotEncoder`) en un solo objeto reutilizable, garantizando que al recibir nuevos datos en producción no ocurra fuga de información (*data leakage*).

---

## 4. Tecnologías y Entorno
- **Lenguaje:** Python 3.12
- **Contenerización:** Docker & Docker Compose (Python 3.12-slim)
- **Librerías Científicas:** NumPy, Pandas, Matplotlib, Seaborn, Scikit-Learn
- **Control de Versiones:** Git & GitHub

---

## 5. Ejecución del Proyecto

### 1. Ejecutar análisis EDA inicial con NumPy:
```bash
python eda_proyecto.py
```

### 2. Ejecutar preparación de datos y gráficos Seaborn:
```bash
python preparacion_datos_pavia.py
```

### 3. Ejecutar dentro del contenedor Docker:
```bash
docker compose up -d
docker exec python_ia python preparacion_datos_pavia.py
```

