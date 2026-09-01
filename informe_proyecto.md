# Informe de Análisis de Datos — Proyecto PAVIA

**Plataforma Inteligente para la Gestión del Deterioro Vial en Cartago, Valle del Cauca**  
**Autores:** Brandon Cortes Giraldo — Johan Sttive Linares Barragán  
**Asignatura:** Inteligencia Artificial (Semestre VI) — COTECNOVA (2026)

---

## 1. Descripción de los Datos

El conjunto de datos analizado contiene 15 registros georreferenciados de daños viales (huecos profundos, grietas longitudinales, hundimientos, baches y fisuras) reportados en diversos barrios representativos del municipio de Cartago (como El Prado, San Jerónimo, Zaragoza, San Nicolás, Álamos, entre otros). Cada registro incluye severidad en escala de 1 a 10, área afectada en metros cuadrados, costo estimado de reparación y nivel de prioridad asignado.

## 2. Estadísticas Clave del Deterioro Vial

| Métrica / Indicador | Valor Calculado |
|---|---|
| **Total de reportes viales analizados** | 15 reportes |
| **Costo total de intervención requerida** | $4,630,000.00 COP |
| **Costo promedio por reparación** | $308,666.67 COP |
| **Área promedio afectada por daño** | 2.33 m² |
| **Nivel de gravedad promedio** | 6.47 / 10.0 |
| **Daño con mayor costo de reparación** | Barrio San Nicolas ($600,000.00 COP - Hueco profundo) |
| **Reportes en prioridad Crítica** | 4 (26.7%) |

## 3. Interpretación de los Resultados para Cartago

1. **Alta Incidencia de Daños Severos:** El promedio de gravedad de **6.47/10** y el hecho de que más del **26.7%** de los casos estén clasificados como críticos evidencian que el deterioro en vías secundarias de Cartago requiere atención inmediata para prevenir accidentes de tránsito (especialmente en motociclistas).
2. **Presupuesto Focalizado:** Con un costo promedio cercano a **$308,667 COP** por punto crítico, el sistema PAVIA permite a la Secretaría de Obras Públicas priorizar los recursos financieros en los puntos de mayor impacto social antes de que el daño aumente su área y costo de bacheo.
3. **Utilidad para Modelos de IA:** Estos datos estructurados servirán como línea base para entrenar los modelos de Visión por Computadora (YOLOv8) y Machine Learning predictivo en las siguientes fases del curso.
