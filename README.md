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

### 2. Ejecutar preparación de datos con Pandas y Seaborn:
```bash
python preparacion_datos_pavia.py
```

### 3. Ejecutar perceptrones y compuertas lógicas (Clase 8):
```bash
python neurona_and.py
python neuronas_logicas.py
```

### 4. Ejecución dentro del contenedor Docker:
```bash
docker compose up -d
docker exec python_ia python preparacion_datos_pavia.py
docker exec python_ia python neuronas_logicas.py
```

---

## 6. Fundamentos de Redes Neuronales: Perceptrón Simple y Compuertas Lógicas (Clase 8)

En concordancia con los objetivos de la **Clase 8: ¿Cómo Aprende una IA? Pesos, Neuronas y Error**, se implementó desde cero y en Python puro (sin librerías de Machine Learning) la arquitectura del **Perceptrón Simple (Rosenblatt, 1958)** en los scripts `neurona_and.py` y `neuronas_logicas.py`.

El objetivo central es comprender el funcionamiento interno del ajuste de parámetros ($w$ y $b$) antes de entrenar redes neuronales profundas en los cortes posteriores de la plataforma **PAVIA**.

```
Entradas (x) ---> [ Pesos (w) ] ---> Suma Ponderada: z = Σ(w_i * x_i) + b ---> [ Función Escalón ] ---> Salida ŷ
```

### A. Modelado Matemático de la Neurona Artificial
1. **Suma Ponderada:** Combinación lineal de las entradas con los pesos sinápticos y el sesgo (*bias*):
   $$z = w_1 x_1 + w_2 x_2 + \dots + w_n x_n + b$$
2. **Función de Activación Escalón (Heaviside):**
   $$\hat{y} = f(z) = \begin{cases} 1 & \text{si } z \ge 0 \\ 0 & \text{si } z < 0 \end{cases}$$
3. **Cálculo del Error:**
   $$\text{error} = y_{\text{real}} - \hat{y}_{\text{pred}}$$
4. **Regla de Aprendizaje del Perceptrón (Descenso del Error):**
   $$w_i \leftarrow w_i + \alpha \cdot \text{error} \cdot x_i$$
   $$b \leftarrow b + \alpha \cdot \text{error}$$
   *(donde $\alpha = 0.1$ representa la tasa de aprendizaje o learning rate).*

---

### B. Adaptación de las Compuertas Lógicas a las Reglas de Decisión de PAVIA

Para contextualizar el aprendizaje supervisado con la problemática vial de Cartago, cada compuerta lógica representa una regla de decisión operativa dentro de PAVIA:

| Compuerta | Regla Operativa en PAVIA | Entradas ($x_1, x_2$) | Salida Esperada ($y$) |
|---|---|---|---|
| **AND** | **Despacho Inmediato de Cuadrilla de Emergencia** | $x_1$: Gravedad Crítica ($\ge 8$)<br>$x_2$: Vía Arterial Principal | **1** únicamente si el daño es crítico Y está sobre una vía principal (ej. San Nicolás/Zaragoza). |
| **OR** | **Agendar Bacheo Preventivo de Vía** | $x_1$: Fisura temprana detectada<br>$x_2$: Proximidad de temporada de lluvias | **1** si al menos una condición se cumple, para evitar que la subbase asfáltica colapse. |
| **NOT** | **Transitabilidad Segura de la Calzada** | $x_1$: Deterioro vial activo en carril | **1** si NO hay daño reportado ($x_1=0$); **0** si la calzada presenta fallas ($x_1=1$). |
| **XOR** | **Decisión Multicriterio Compleja (No Lineal)** | $x_1$: Prioridad de Tráfico<br>$x_2$: Presupuesto Reducido | **1** solo para casos asimétricos. Demuestra el límite del perceptrón simple. |

---

### C. Resultados del Entrenamiento y Convergencia

Se simuló el aprendizaje iterativo por épocas en `neuronas_logicas.py`, registrando la evolución del error total acumulado:

* **Compuerta AND:** Convergió en **3 épocas** con parámetros finales $w_1 = 0.200$, $w_2 = 0.100$, $b = -0.200$.
* **Compuerta OR:** Convergió en **2 épocas** con parámetros finales $w_1 = 0.100$, $w_2 = 0.200$, $b = -0.100$.
* **Compuerta NOT:** Convergió en **4 épocas** con parámetros finales $w_1 = -0.100$, $b = 0.000$.
* **Compuerta XOR:** **No convergió**. El error total osciló entre 2 y 4 a lo largo de las 15 épocas sin alcanzar jamás el error 0.

*(Los resultados gráficos del descenso del error se encuentran consolidados en `evolucion_error_compuertas.png`).*

---

### D. Respuestas a las Preguntas Teóricas de la Rúbrica (Clase 8 - Pág. 12)

#### 1. ¿Cuántas épocas necesitó cada compuerta para aprender?
* **OR:** 2 épocas. Fue la más rápida en converger debido a que 3 de las 4 combinaciones tienen como objetivo la clase positiva ($1$).
* **AND:** 3 épocas. Requirió un ajuste adicional en el bias para volverlo lo suficientemente negativo y filtrar los casos $(0,1)$ y $(1,0)$.
* **NOT:** 4 épocas. Necesitó invertir el signo del peso sináptico inicial ($w_1$) a un valor negativo ($-0.100$) para producir la inversión lógica.
* **XOR:** No converge independientemente del número de épocas.

#### 2. ¿Fue necesario ajustar la tasa de aprendizaje ($\alpha$)? ¿Por qué?
Se utilizó una tasa de aprendizaje estándar $\alpha = 0.1$, la cual resultó óptima para garantizar estabilidad matemática. 
* Si se incrementa $\alpha$ a valores elevados ($\ge 1.0$), los pesos sufren oscilaciones bruscas y pueden saltar repetidamente la frontera de decisión sin estabilizarse.
* Si $\alpha$ se reduce en exceso ($\le 0.001$), los pasos de gradiente son microscópicos y la neurona requeriría cientos de épocas innecesarias para converger en un espacio de búsqueda tan pequeño.

#### 3. ¿Qué diferencias encontró entre la compuerta AND y la OR?
La diferencia matemática fundamental radica en el **sesgo (*bias* $b$) y la posición espacial de la recta separadora**:
* En la compuerta **OR**, el sesgo es poco restrictivo ($b = -0.100$); basta con que una sola de las entradas sea positiva para que el producto $w_i x_i$ supere el umbral cero ($z \ge 0$).
* En la compuerta **AND**, el sesgo es fuertemente negativo ($b = -0.200$); actúa como una barrera estricta que exige la suma simultánea de ambas entradas activas ($w_1(1) + w_2(1) = 0.300 > 0.200$) para activar la neurona.

#### 4. ¿Por qué la compuerta XOR no puede ser aprendida por una sola neurona?
Esta limitación corresponde al histórico dilema de la **separabilidad lineal** planteado por Marvin Minsky y Seymour Papert en 1969:
1. En un espacio euclidiano bidimensional, un perceptrón simple solo puede trazar **una única línea recta de decisión** definida por la ecuación:
   $$w_1 x_1 + w_2 x_2 + b = 0$$
2. Para la compuerta XOR, las salidas verdaderas ($y=1$) se encuentran en las coordenadas diagonales opuestas $(0,1)$ y $(1,0)$, mientras que las salidas falsas ($y=0$) se sitúan en $(0,0)$ y $(1,1)$.
3. **Imposibilidad geométrica:** Es matemáticamente imposible trazar una sola recta que aísle simultáneamente los puntos $\{(0,1), (1,0)\}$ de los puntos $\{(0,0), (1,1)\}$.
4. **Implicación en PAVIA:** Para clasificar decisiones viales complejas que dependen de interacciones no lineales entre variables (por ejemplo, evaluar gravedad combinada con densidad de tráfico y tipos de asfalto), un perceptrón simple es insuficiente. Se hace indispensable implementar **Redes Neuronales Multicapa (Multilayer Perceptron - MLP)** con capas ocultas y funciones de activación no lineales continuas (como Sigmoide o ReLU), las cuales se abordarán en los próximos cortes del proyecto.

---

### E. Instrucciones de Ejecución de las Neuronas Lógicas:
```bash
# Ejecutar neurona AND:
python neurona_and.py

# Ejecutar compuertas lógicas (OR, NOT, AND, XOR) y generar gráfico:
python neuronas_logicas.py
```


