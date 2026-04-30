# ------------------- Importaciones

import pandas as pd

# ------------------- Fin de las Importaciones

"""carga de archivos"""
happiness = pd.read_csv(r"Happiness_report.csv")
metadata = pd.read_csv(r"Metadata.csv")

"""se agregan estas opciones para verificar cada uno de los dfs"""
print(happiness.info())
print(happiness.columns)
print(happiness.dtypes)
print(happiness.shape)

print(metadata.info())
print(metadata.columns)
print(metadata.dtypes)
print(metadata.shape)