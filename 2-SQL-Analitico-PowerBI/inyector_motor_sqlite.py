import pandas as pd
import sqlite3

# 1. Rutas corregidas apuntando a tu nueva carpeta 'sql y power bi'
df_hechos = pd.read_csv("sql y power bi/hechos_comisiones.txt")
df_dim = pd.read_csv("sql y power bi/dim_asesores.txt")

# 2. Crear o conectar a la base de datos física del proyecto
conn = sqlite3.connect("sql y power bi/auditoria_comercial.db")

# 3. Forzar la inyección y creación directa en el motor SQL
df_hechos.to_sql("hechos_comisiones", conn, if_exists="replace", index=False)
df_dim.to_sql("dim_asesores", conn, if_exists="replace", index=False)

print("¡Tablas 'hechos_comisiones' y 'dim_asesores' cargadas con éxito en auditoria_comercial.db!")
conn.close()

