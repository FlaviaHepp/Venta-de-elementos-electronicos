
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
plt.style.use('dark_background')
from matplotlib.ticker import FormatStrFormatter


vta_elect = pd.read_csv('ventas_electronica.csv')
print(vta_elect)

vta_elect["Fecha de Venta"] = pd.to_datetime(vta_elect["Fecha de Venta"])


#Limpieza de datos
print(vta_elect.isna())
print("\nCantidad de datos faltantes por columnas\n", vta_elect.isna().sum())


ventas = vta_elect.dropna()
ventas = ventas[
    (ventas["Cantidad Vendida"] > 0) &
    (ventas["Cantidad Vendida"].astype(float) == ventas["Cantidad Vendida"].astype(int)) &
    (ventas["Precio Unitario"] > 0)]

print(ventas)

print("\nCantidad de datos faltantes por columnas\n", ventas.isna().sum())


#Ventas totales de cámaras
condicion = ventas["Producto Vendido"].str.contains("Cámara")
ventas[condicion]
ventas[condicion]["Cantidad Vendida"].sum()

print("\nVenta total de ", ventas[condicion]["Cantidad Vendida"].sum(), "cámaras\n")


#Ventas realizadas entre tal y tal fecha
def busqueda(ventas, inicio, fin):
  condicion1 = ventas["Fecha de Venta"] >= inicio
  condicion2 = ventas["Fecha de Venta" ] <= fin
  rango = ventas.loc[condicion1 & condicion2]

  return(rango)


print("Ingrese las fechas con formato YYYY-MM-DD")

inicio = input("Ingrese una fecha: ")
fin = input("Ingrese una segunda fecha: ")

rango = busqueda(ventas, inicio, fin)
print("Resultados de la búsqueda:\n\n")
print(rango)


#Venta de productos que superaron las 10 unidades en el mes de agosto durante el 2023
condicion1 = ventas["Fecha de Venta"] >= "2023-08-01"
condicion2 = ventas["Fecha de Venta"] <= "2023-08-31"
condicion3 = ventas["Cantidad Vendida"] > 10

print("\nCantidad: \n", ventas.loc[ condicion1 & condicion2 & condicion3])

#Análisis de ventas mensuales
ventas.groupby(ventas["Fecha de Venta"].dt.month)["Cantidad Vendida"].sum()

#Agrupado ventas por mes
ventas_agrupado = ventas.groupby(ventas["Fecha de Venta"].dt.month)

#Sumo ventas por mes
ventas_por_mes = ventas_agrupado["Cantidad Vendida"].sum()

#Gráfico
fig, ax = plt.subplots(figsize=(15,15))
meses = ["Agosto", "Septiembre", "Octubre"]

ventas_por_mes.plot.bar(facecolor='lavender', edgecolor = "mediumpurple", linewidth = 2)
plt.xticks(rotation= 360)
plt.xlabel('\nMes\n', fontsize = 12)
plt.ylabel('\nCantidad\n', fontsize = 12)
plt.title("\nAnálisis de ventas mensuales\n", fontsize = 16)
ax.set_xticklabels(meses)

for bar in ax.patches:
  ax.text(bar.get_x() + bar.get_width() / 2,
          bar.get_height() / 2 + bar.get_y(),
          round(bar.get_height()), ha = 'center',
          color = 'rebeccapurple', weight = 'bold', size = 11)

plt.grid(color='grey', linestyle='-', linewidth=0.25, alpha=0.5)
plt.show()