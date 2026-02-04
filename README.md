# Venta-de-elementos-electronicos
Análisis y visualización de venta de elementos electrónicos.

Se ingresó a Python y se visualizó el archivo ventas_electronica.csv, utilizando la librería de Pandas. Este dataset, contiene información sobre datos de ventas de artículos electrónicos. Se Realizó un análisis exploratorio de datos del Dataframe, especificando los principales hallazgos. Para desarrollar a profundidad el análisis se buscó dar respuestas a algunas inquietudes. 
Mediante la biblioteca de Matplotlib, se confeccionó una visualización de datos con su correspondiente interpretación. 
Por último, se generó una pequeña conclusión del análisis efectuado.

# Análisis de ventas electrónicas

Este proyecto realiza un **análisis exploratorio y descriptivo de ventas de productos electrónicos**, utilizando Python y pandas, con el objetivo de **entender el comportamiento de las ventas a lo largo del tiempo** y responder preguntas clave de negocio.

El análisis incluye limpieza de datos, filtrado por condiciones, consultas por rango de fechas y visualización de ventas mensuales.

---

## 🛒 Contexto del negocio

Las empresas de venta de productos electrónicos necesitan analizar:
- qué productos se venden más
- en qué períodos se concentran las ventas
- cómo evoluciona la demanda mes a mes

Este proyecto analiza un dataset de ventas reales para **apoyar la toma de decisiones comerciales**.

---

## 🎯 Objetivos del análisis

- Limpiar y preparar datos de ventas
- Analizar ventas totales por producto
- Identificar productos con mayor volumen de ventas
- Evaluar ventas en rangos de fechas específicos
- Visualizar la evolución mensual de ventas

---

## 📊 Dataset

El dataset contiene información de ventas de productos electrónicos.

### Variables principales
- `Fecha de Venta`
- `Producto Vendido`
- `Cantidad Vendida`
- `Precio Unitario`

---

## 🧹 Limpieza y preparación de datos

Se realizaron los siguientes pasos:
- Conversión de la columna `Fecha de Venta` a formato datetime
- Eliminación de valores nulos
- Filtrado de:
  - cantidades negativas o nulas
  - cantidades no enteras
  - precios unitarios inválidos

Estas transformaciones garantizan la **consistencia y calidad de los datos**.

---

## 🔍 Análisis realizados

- **Ventas totales de cámaras**
- Búsqueda de ventas entre rangos de fechas ingresados por el usuario
- Identificación de productos con más de 10 unidades vendidas en agosto de 2023
- Análisis de ventas agregadas por mes

---

## 📈 Visualizaciones

- Gráfico de barras de ventas mensuales
- Etiquetado automático de valores en gráficos
- Análisis comparativo entre meses

Los gráficos permiten una **interpretación clara del comportamiento de ventas**.

---

## 📌 Principales insights

- Las ventas presentan variaciones significativas entre meses
- Determinados productos concentran mayores volúmenes de ventas
- El análisis temporal facilita la detección de picos de demanda

---

## 🛠️ Tecnologías utilizadas

- **Python**
- **pandas**
- **matplotlib**
- **NumPy**

---

## 📂 Estructura del repositorio

├── ventas_electronica.csv
├── Análisis de ventas electrónicas.py
├── README.md


---

## 🚀 Próximos pasos

- Incorporar análisis de ingresos (cantidad × precio)
- Comparar desempeño por categoría de producto
- Crear dashboards interactivos
- Automatizar reportes mensuales

---

## 👤 Autor

**Flavia Hepp**  
Data Analyst en formación  
