# Este programa carga un archivo de Excel llamado "calificaciones_alumnos.xlsx",
# agrega una nueva columna llamada "Mat_Fisica" con valores aleatorios entre 0 y 100
# con un decimal, y guarda el archivo actualizado.

import pandas as pd
import numpy as np

# Cargar el archivo Excel
file_path = 'calificaciones_alumnos.xlsx'
df = pd.read_excel(file_path)

# Generar valores aleatorios para la columna "Mat_Fisica"
np.random.seed(0)  # Fijar la semilla para reproducibilidad
df['Mat_Fisica'] = np.round(np.random.uniform(0, 100, len(df)), 1)

# Guardar el archivo actualizado
df.to_excel('calificaciones_alumnos_actualizado.xlsx', index=False)
