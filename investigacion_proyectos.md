# Investigación de Proyectos de Inteligencia Artificial

**Asignatura:** Inteligencia Artificial (Semestre 6)  
**Institución:** COTECNOVA  
**Estudiantes:** Brandon Cortes Giraldo — Johan Sttive Linares Barragán  
**Actividad:** Actividad Independiente - Clase 1 (Exploración del Banco de Proyectos)

---

## Introducción

El presente documento contiene el análisis e investigación preliminar de tres (3) propuestas de proyectos de Inteligencia Artificial orientadas a resolver problemáticas reales del municipio de Cartago, Valle del Cauca (Colombia). Cada propuesta ha sido diseñada integrando componentes de Machine Learning, Deep Learning, IA Generativa y Ciencia de Datos, con el objetivo de construir soluciones funcionales, documentadas y con impacto social, redactadas en un lenguaje claro y accesible.

---

## Proyecto 1: PAVIA — Plataforma Inteligente de Gestión del Deterioro Vial (⭐ Propuesta Principal)

* **¿Qué problema resuelve?:**  
  El municipio de Cartago presenta un deterioro significativo en su malla vial. Los huecos, grietas y hundimientos en las calles generan accidentes de tránsito, deterioro de vehículos (especialmente motocicletas) y afectan la movilidad de los ciudadanos. Actualmente, no existe un sistema centralizado que permita a los ciudadanos reportar estos daños, ni una herramienta que ayude a la administración municipal a priorizar las reparaciones de manera objetiva e inteligente.

* **¿Qué tipo de datos se necesitarían?:**  
  Imágenes de daños viales obtenidas de datasets públicos (Kaggle, Roboflow), datos geográficos de los barrios y vías de Cartago, y datos climáticos históricos del IDEAM (precipitación, temperatura) para alimentar el módulo de predicción de deterioro futuro.

* **¿Qué modelo de IA podría ser adecuado?:**  
  **YOLOv8** (Visión por Computadora) para detectar automáticamente el tipo de daño en fotografías (hueco, grieta, hundimiento). **Random Forest** (Scikit-Learn) para predecir qué vías tienen mayor probabilidad de deteriorarse según su historial y condiciones climáticas. Un **motor de reglas** en Python puro para calcular gravedad, riesgo vehicular y costo estimado de reparación. **IA Generativa** (Hugging Face) para un chatbot que permita a los funcionarios consultar el sistema en lenguaje natural.

* **Tecnologías:** Python, Flask, YOLOv8 (Ultralytics), OpenCV, PyTorch, Scikit-Learn, Pandas, NumPy, Matplotlib, Chart.js, Leaflet/Folium, SQLite, SQLAlchemy, Bootstrap 5, HTML5, CSS3, JavaScript, Git/GitHub.

---

## Proyecto 2: EcoCartago AI — Clasificación Inteligente de Residuos Sólidos en Tiempo Real

* **¿Qué problema resuelve?:**  
  En el municipio de Cartago, al igual que en gran parte de Colombia, la separación de residuos sólidos desde la fuente es deficiente. Los ciudadanos desconocen la clasificación correcta de los residuos (orgánicos, reciclables, electrónicos, peligrosos), lo que genera sobrecarga en los rellenos sanitarios, contaminación ambiental y pérdida de materiales que podrían ser reutilizados.

* **¿Qué tipo de datos se necesitarían?:**  
  Datasets públicos de clasificación de residuos disponibles en Kaggle, que contienen miles de imágenes etiquetadas de objetos como plástico, vidrio, cartón, metal, residuos orgánicos y electrónicos.

* **¿Qué modelo de IA podría ser adecuado?:**  
  **Redes Neuronales Convolucionales (CNN)** con TensorFlow/Keras para clasificar imágenes de residuos en tiempo real a través de la cámara web del usuario. **Scikit-Learn** para el cálculo de métricas de evaluación (precisión, recall, matrices de confusión). **IA Generativa** (Hugging Face) como asistente virtual que explica al usuario cómo preparar cada tipo de residuo antes de reciclarlo.

* **Tecnologías:** Python, Flask, TensorFlow/Keras, OpenCV, Scikit-Learn, Pandas, NumPy, Matplotlib, Bootstrap 5, HTML5, CSS3, JavaScript, Git/GitHub.

---

## Proyecto 3: Agro-IA Norte del Valle — Plataforma Predictiva para Pequeños Agricultores

* **¿Qué problema resuelve?:**  
  La economía de Cartago y el norte del Valle del Cauca depende en gran medida de la actividad agrícola. Sin embargo, los pequeños productores enfrentan pérdidas económicas significativas debido a factores climáticos impredecibles, plagas y la falta de asistencia técnica oportuna. Muchos agricultores no cuentan con herramientas tecnológicas que les permitan anticipar riesgos y tomar mejores decisiones sobre sus cultivos.

* **¿Qué tipo de datos se necesitarían?:**  
  Datos climáticos históricos del IDEAM (temperatura, precipitación, humedad), datos de tipos de suelo de la región y registros de comportamiento de cultivos representativos del norte del Valle (café, plátano, caña).

* **¿Qué modelo de IA podría ser adecuado?:**  
  **Random Forest / Gradient Boosting** (Scikit-Learn) para predicción de riesgos agrícolas basándose en variables climáticas e históricas. **Redes neuronales** (TensorFlow/Keras) para análisis de series de tiempo climáticas. **IA Generativa** (Hugging Face) para generar reportes escritos en lenguaje sencillo dirigidos al agricultor, traduciendo los resultados técnicos a recomendaciones prácticas.

* **Tecnologías:** Python, Flask, Scikit-Learn, TensorFlow/Keras, Pandas, NumPy, Matplotlib, Seaborn, Folium/Leaflet, Chart.js, Bootstrap 5, HTML5, CSS3, JavaScript, Git/GitHub.

---

## Cuadro Comparativo

| Criterio | PAVIA | EcoCartago AI | Agro-IA Norte del Valle |
|---|---|---|---|
| Área de IA principal | Visión por Computadora | Clasificación de imágenes (CNN) | ML Predictivo |
| Dificultad técnica | Media-Alta | Media | Media |
| Impacto social | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐⭐ |
| Facilidad de conseguir datos | ⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐ |
| Componente visual | Mapa + Dashboard | Cámara en tiempo real | Gráficas + Mapa |
| Integración de IA Generativa | Chatbot de consultas | Asistente de reciclaje | Reportes automáticos |
| Escalabilidad | Muy alta | Alta | Alta |

---

## Conclusión

Las tres propuestas presentadas están alineadas con los objetivos de la asignatura de Inteligencia Artificial y abordan problemáticas reales y vigentes del municipio de Cartago, Valle del Cauca. Cada una integra componentes de Machine Learning, Deep Learning, IA Generativa y Ciencia de Datos, cumpliendo con los requisitos técnicos establecidos.

Nuestra propuesta principal es **PAVIA**, ya que representa un sistema integral de apoyo a la gestión pública con alto potencial de impacto, escalabilidad y diferenciación académica. No obstante, las tres ideas son viables y pueden ser desarrolladas de manera incremental a lo largo del semestre, siguiendo la metodología de Aprendizaje Basado en Proyectos (ABP).

Quedamos atentos a la retroalimentación del docente para definir la propuesta definitiva y dar inicio formal al desarrollo del proyecto.
