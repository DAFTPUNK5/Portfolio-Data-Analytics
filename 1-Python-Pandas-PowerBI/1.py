import pandas as pd

tx1 = pd.read_csv("pandas y power bi/auditoria_transacciones.txt")

tx2 = pd.read_csv("pandas y power bi/maestro_sedes.txt")

tx2 = tx2.rename(columns={"cod_vendedor":"id_vendedor"})

df = pd.merge(tx1,tx2,on="id_vendedor",how="left")
# print(df)

df["nombre_comercial"] = df["nombre_comercial"].fillna("EXTERNO_NO_REGISTRADO")
df["region_banco"] = df["region_banco"].fillna("SEDE_BAJO_INVESTIGACION")
df["canal_venta"] = df["canal_venta"].fillna("OTROS")
# print(df)

df = df.drop_duplicates(subset=["id_ticket"])
# print(df)

df["region_banco"] = df["region_banco"].str.upper()
# print(df)

df_pivot = df.pivot_table(index="region_banco",columns="canal_venta",values="monto_bruto",aggfunc="sum",fill_value=0)
# print(df_pivot)

df_final = df_pivot.reset_index()
print(df_final)

df_final.to_csv("auditoria_senior_limpia.csv",index=False)