# Este programa carga un archivo de Excel llamado "calificaciones_alumnos.xlsx",
# lee los datos de calificaciones de los alumnos y crea un gráfico de barras para
# visualizar las calificaciones en diferentes materias sin que las etiquetas en el
# eje X se encimen.

import pandas as pd
import matplotlib.pyplot as plt

# Cargar el archivo Excel
file_path = 'calificaciones_alumnos.xlsx'
df = pd.read_excel(file_path)

# Nombres de los alumnos
nombres = df['Nombre']

# Calificaciones en diferentes materias
calculo_integral = df['Mat_CalculoIntegral']
programacion_oop = df['Mat_ProgramacionOOP']
estructura_datos = df['Mat_EstructuraDatos']

# Configurar el gráfico de barras
fig, ax = plt.subplots(figsize=(10, 6))

# Posiciones de las barras en el eje X
bar_width = 0.2
bar_positions = list(range(len(nombres)))

# Dibujar las barras para cada materia
ax.bar(bar_positions, calculo_integral, width=bar_width, label='Cálculo Integral', align='center')
ax.bar([p + bar_width for p in bar_positions], programacion_oop, width=bar_width, label='Programación OOP', align='center')
ax.bar([p + 2 * bar_width for p in bar_positions], estructura_datos, width=bar_width, label='Estructura de Datos', align='center')

# Configuración de las etiquetas en el eje X
ax.set_xticks([p + bar_width for p in bar_positions])
ax.set_xticklabels(nombres, rotation=45, ha='right')

# Añadir leyenda y etiquetas
ax.set_xlabel('Alumnos')
ax.set_ylabel('Calificaciones')
ax.set_title('Calificaciones de los Alumnos en Diferentes Materias')
ax.legend()

# Mostrar gráfico
plt.tight_layout()
plt.show()
