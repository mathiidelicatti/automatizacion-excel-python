import os
import pandas as pd 
#Carpeta donde estan los excels 
carpeta = 'VENTAS'

#Lista de archivos en la carpeta
archivo = os.listdir(carpeta)
print(archivo)

#Filtrar solo archivos.xlsx
archivos_excels = [f for f in archivo if f.endswith('xlsx')]

#Lista para guardar DataFrames 
dfs = []

#Leer cada archivo
for archivo in archivos_excels :
    ruta = os.path.join(carpeta,archivo)
    df = pd.read_excel(ruta)
    dfs.append(df)
print(df)

#Unir todos los DataFrames
df_total = pd.concat(dfs, ignore_index= True)
print(df_total)

#Crear columnas nuevas 
df_total['IVA'] = df_total['PRECIO'] * 0.21
df_total['PRECIO_FINAL'] = df_total['PRECIO'] + df_total['IVA']

#Agrupar por producto 

resumen = df_total.groupby('PRODUCTO')['PRECIO_FINAL'].sum().reset_index()

#Ordenar resultados
resumen = resumen.sort_values(by='PRECIO_FINAL',ascending= False)

#Agregar filtros
top3 = resumen.head(3)
print(top3)

ventas_grandes = df_total[df_total['PRECIO'] > 100]
#Exportar resultados

df_total.to_excel('Ventas_completadas.xlsx', index= False)
resumen.to_excel('Reporte_final.xlsx', index= False)
ventas_grandes.to_excel('ventas_grandes.xlsx', index = False)