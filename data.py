# Criando dataset Iris manualmente (caso não tenha acesso ao sklearn)
import random
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import sklearn.datasets as datasets

# Dados simplificados do Iris para demonstração
iris_data = {
    'sepal_length': [5.1, 4.9, 4.7, 4.6, 5.0, 5.4, 4.6, 5.0, 4.4, 4.9,
                     7.0, 6.4, 6.9, 5.5, 6.5, 5.7, 6.3, 4.9, 6.6, 5.2,
                     6.3, 5.8, 7.1, 6.3, 6.5, 7.6, 4.9, 7.3, 6.7, 7.2],
    'sepal_width':  [3.5, 3.0, 3.2, 3.1, 3.6, 3.9, 3.4, 3.4, 2.9, 3.1,
                     3.2, 3.2, 3.1, 2.3, 2.8, 2.8, 3.3, 2.4, 2.9, 2.7,
                     3.3, 2.7, 3.0, 2.9, 3.0, 3.0, 2.5, 2.9, 2.5, 3.6],
    'petal_length': [1.4, 1.4, 1.3, 1.5, 1.4, 1.7, 1.4, 1.5, 1.4, 1.5,
                     4.7, 4.5, 4.9, 4.0, 4.6, 4.5, 4.7, 3.3, 4.6, 3.9,
                     6.0, 5.1, 5.9, 5.6, 5.8, 6.6, 4.5, 6.3, 5.8, 6.1],
    'petal_width':  [0.2, 0.2, 0.2, 0.2, 0.2, 0.4, 0.3, 0.2, 0.2, 0.1,
                     1.4, 1.5, 1.5, 1.3, 1.5, 1.3, 1.6, 1.0, 1.3, 1.4,
                     2.5, 1.9, 2.1, 1.8, 2.2, 2.1, 1.7, 1.8, 1.8, 2.5],
    'species': ['setosa']*10 + ['versicolor']*10 + ['virginica']*10
}
df_iris = pd.DataFrame(iris_data)

print(df_iris.head())  # Mostra as 5 primeiras linhas
print(df_iris.head(10))  # Mostra as 10 primeiras
print(df_iris.tail())  # Mostra as 5 últimas linhas
print(df_iris.info())
print(df_iris.describe())
print(df_iris.columns)
print(df_iris['species'].unique())
print(df_iris['species'].value_counts())
print(df_iris.isnull().sum())
sns.pairplot(df_iris, hue="species")
plt.show()