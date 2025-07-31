# Creating Iris dataset manually (if sklearn is not available)
import random
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


# Simplified Iris data for demonstration
iris_data = {
    'sepal_length': [5.1, 4.9, 4.7, 4.6, 5.0, 5.4, 4.6, 5.0, 4.4, 4.9,
                     7.0, 6.4, 6.9, 5.5, 6.5, 5.7, 6.3, 4.9, 6.6, 5.2,
                     6.3, 5.8, 7.1, 6.3, 6.5, 7.6, 4.9, 7.3, 6.7, 7.2],
    'sepal_width': [3.5, 3.0, 3.2, 3.1, 3.6, 3.9, 3.4, 3.4, 2.9, 3.1,
                    3.2, 3.2, 3.1, 2.3, 2.8, 2.8, 3.3, 2.4, 2.9, 2.7,
                    3.3, 2.7, 3.0, 2.9, 3.0, 3.0, 2.5, 2.9, 2.5, 3.6],
    'petal_length': [1.4, 1.4, 1.3, 1.5, 1.4, 1.7, 1.4, 1.5, 1.4, 1.5,
                     4.7, 4.5, 4.9, 4.0, 4.6, 4.5, 4.7, 3.3, 4.6, 3.9,
                     6.0, 5.1, 5.9, 5.6, 5.8, 6.6, 4.5, 6.3, 5.8, 6.1],
    'petal_width': [0.2, 0.2, 0.2, 0.2, 0.2, 0.4, 0.3, 0.2, 0.2, 0.1,
                    1.4, 1.5, 1.5, 1.3, 1.5, 1.3, 1.6, 1.0, 1.3, 1.4,
                    2.5, 1.9, 2.1, 1.8, 2.2, 2.1, 1.7, 1.8, 1.8, 2.5],
    'species': ['setosa']*10 + ['versicolor']*10 + ['virginica']*10
}
df_iris = pd.DataFrame(iris_data)

print(df_iris.head(10))  # Mostra as 5 primeiras linhas
print(df_iris.tail())  # Mostra as 5 últimas linhas
print(df_iris.info())
print(df_iris.describe())
print(df_iris.columns)
print(df_iris['species'].unique())
print(df_iris['species'].value_counts())
print(df_iris.isnull().sum())
duplicatas = df_iris.duplicated()
print("Total de duplicatas:", duplicatas.sum())
df_iris = df_iris.rename(columns={
    'sepal_length': 'comprimento_sepala',
    'sepal_width': 'largura_sepala',
    'petal_length': 'comprimento_petala',
    'petal_width': 'largura_petala',
    'species': 'especie'
})
print(df_iris.columns)
print(df_iris.head())
# Agrupar por espécie
grupo_especie = df_iris.groupby('especie')
# Aplicando média por espécie
media_por_especie = grupo_especie.mean(numeric_only=True)
print("Média por espécie:\n", media_por_especie)

# Aplicando desvio padrão por espécie
std_por_especie = grupo_especie.std(numeric_only=True)
print("\nDesvio padrão por espécie:\n", std_por_especie)
# Função personalizada: intervalo (amplitude) dos valores
def intervalo(x):
    return x.max() - x.min()

intervalo_por_especie = grupo_especie.agg(intervalo)
print("\nIntervalo (máx - mín) por espécie:\n", intervalo_por_especie)
# Função personalizada: média com 2 casas decimais
def media_arredondada(x):
    return round(x.mean(), 2)

media_arredondada_por_especie = grupo_especie.agg(media_arredondada)
print("\nMédia arredondada por espécie:\n", media_arredondada_por_especie)
virginica = df_iris[df_iris['especie'] == 'virginica']
print("Dados da espécie virginica:\n", virginica)
print("\nMédia da espécie virginica:")
print(virginica.mean(numeric_only=True))

# cores por especie
cores = {'setosa': 'red', 'versicolor': 'green', 'virginica': 'blue'}

# Criando o gráfico
plt.figure(figsize=(8, 6))

for especie in df_iris['especie'].unique():
    subset = df_iris[df_iris['especie'] == especie]
    plt.scatter(subset['comprimento_petala'], subset['largura_petala'],
                label=especie, color=cores[especie])

plt.title("Comprimento vs Largura da Pétala por Espécie")
plt.xlabel("Comprimento da Pétala (cm)")
plt.ylabel("Largura da Pétala (cm)")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()