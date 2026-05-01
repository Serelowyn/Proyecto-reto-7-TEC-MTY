# ------------------- Importaciones

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# ------------------- Fin de las Importaciones

"""carga de archivos"""
happiness = pd.read_csv(r"Happiness_report.csv")
metadata = pd.read_csv(r"Metadata.csv")

"""se agregan estas opciones para verificar cada uno de los dfs"""
print(happiness.info())
print(happiness.columns)
print(happiness.dtypes)
print(happiness.shape)
print(happiness.head())

print(metadata.info())
print(metadata.columns)
print(metadata.dtypes)
print(metadata.shape)
print(metadata.head())

"""se agrega df de mexico unicamente con la informacion de mx"""
mexico = happiness.loc[happiness["Country or region"] == "Mexico"].set_index("Country or region")
print(mexico)

"""4.	Obtén un histograma del puntaje (score) para identificar el rango o clase más frecuente. Ubica el valor de México con una etiqueta de texto. """

plt.figure(figsize=(8,5))
n, bins, patches = plt.hist(happiness["Score"], color="C0", edgecolor="k")
mex_score = float(mexico["Score"].iloc[0])
plt.axvline(mex_score, color='red', linestyle=":", linewidth=2)
plt.text(mex_score + 0.02, max(n) * 0.9, f"mexico: {mex_score}", color="red")
plt.title("histograma happiness score de 2019")
plt.xlabel("score")
plt.ylabel("frecuencia")

"""5.	Construye un boxplot para la columna esperanza de vida (Healthy life expectancy). Ubica el valor de México con una anotación."""

plt.figure(figsize=(8,4))
sns.boxplot(x=happiness["Healthy life expectancy"], color="C2")
salud_mex = float(mexico["Healthy life expectancy"].iloc[0])

#anotacion mex
plt.scatter(salud_mex, 0, color="red", zorder=10)
plt.annotate(f"mexico: {salud_mex}", xy=(salud_mex, 0), xytext=(salud_mex+0.05, 0.15), arrowprops=dict(arrowstyle="->", color="red"))
plt.title("healthy life expectancy")
plt.xlabel("años")
plt.yticks([])
plt.show()

"""6.	Crea una gráfica circular para analizar en qué medida los factores contribuyen a evaluar la felicidad en México. Para ello, deberás modificar la estructura del dataframe mexico, obtenido anteriormente."""

mexico.columns

factors = [
    "GDP per capita",
    "Perceptions of corruption",
    "Social support",
    "Healthy life expectancy",
    "Freedom to make life choices",
    "Generosity",
]

mexico_circulo = happiness.loc[happiness["Country or region"] == "Mexico", factors].iloc[0]
mexico_factors = mexico_circulo.rename(index={"GDP per capita":"GDP per capita",
    "Social support":"Social support",
    "Healthy life expectancy":"Healthy life expectancy",
    "Freedom to make life choices":"Freedom",
    "Generosity":"Generosity",
    "Perceptions of corruption":"Corruption"
})

values = mexico_factors.values
total = values.sum()
percentages = values / total * 100

#grafico
fig, ax = plt.subplots(figsize=(12,7))
ax.pie(percentages, labels=mexico_factors.index, autopct="%1.1f%%", startangle=90, colors=sns.color_palette("Set2"))
ax.set_title("contribucion relativa de factores en mexico", fontsize=14, loc="left")
ax.axis("equal")
plt.tight_layout()
plt.show()

"""7.	Filtra el dataframe para quedarte con 5 países (el más feliz, el menos feliz, México y dos más de tu interés) y visualiza en una misma gráfica los 6 factores."""

#finland 1
#south sudan 156
#mexico
#costa rica
#brazil

paises = ["Finland", "South Sudan", "Mexico", "Costa Rica", "Brazil"]
graf = happiness[happiness["Country or region"].isin(paises)].set_index("Country or region")[factors]
graf.plot(kind="bar", figsize=(12,6))
plt.title("comparativa de factores de 5 paises")
plt.ylabel("contribucion")
plt.xticks(rotation=45)
plt.legend(loc="upper right", bbox_to_anchor=(1.25, 1))
plt.tight_layout()
plt.show()

"""8.	Crea una matriz de subgráficas de 2 x 3 con scatter plots del puntaje (score) versus los 6 factores, para determinar qué factor influye más en la evaluación."""

fig, axes = plt.subplots(2, 3, figsize=(12,6))
axes = axes.flatten()

for i, f in enumerate(factors):
    sns.scatterplot(ax=axes[i], data=happiness, x=f, y="Score", color=f"C{i}")
    axes[i].set_title(f"Score vs {f}")
    axes[i].set_xlabel(f)
    axes[i].set_ylabel("Score")

plt.suptitle("score vs factores 2x3", fontsize=16)
plt.tight_layout(rect=[0, 0.03, 1, 0.95])
plt.show()

"""9.	Comprueba lo anterior con un heatmap donde incluyas los índices de correlación."""

cols_corr = ["Score"] + factors
corr = happiness[cols_corr].corr()
plt.figure(figsize=(8,6))
sns.heatmap(corr, annot=True, fmt=".2f", cmap="inferno", vmin=-1, vmax=1)
plt.title("correlación: score - factores")
plt.show()

