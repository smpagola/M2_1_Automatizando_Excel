# Este programa carga un archivo de Excel llamado "calificaciones_alumnos.xlsx",
# agrega una nueva columna llamada "Mat_Fisica" con valores aleatorios entre 0 y 100
# con un decimal, ordena la tabla por el campo "Nombre", imprime la cantidad de registros
# y campos en la tabla, identifica los campos numéricos, e imprime sus nombres, y guarda
# el archivo actualizado.

import pandas as pd
import numpy as np

# Cargar el archivo Excel
file_path = 'calificaciones_alumnos.xlsx'
df = pd.read_excel(file_path)

# Generar valores aleatorios para la columna "Mat_Fisica"
np.random.seed(0)  # Fijar la semilla para reproducibilidad
df['Mat_Fisica'] = np.round(np.random.uniform(0, 100, len(df)), 1)

# Ordenar el DataFrame por el campo "Nombre"
df_sorted = df.sort_values(by='Nombre')

# Imprimir la cantidad de registros y campos
num_registros = df_sorted.shape[0]
num_campos = df_sorted.shape[1]
print(f'Cantidad de registros: {num_registros}')
print(f'Cantidad de campos: {num_campos}')

# Identificar e imprimir los campos numéricos
numeric_fields = df_sorted.select_dtypes(include=[np.number]).columns.tolist()
print(f'Campos numéricos: {numeric_fields}')

# Guardar el archivo actualizado
df_sorted.to_excel('calificaciones_alumnos_actualizado.xlsx', index=False)
