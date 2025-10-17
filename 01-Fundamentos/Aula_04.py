import pandas as pd
import numpy as np

# 1. DataFrame apenas com mulheres
df_mulheres = df[df['Sex'] == 'female']
print("--- Mulheres a bordo (head) ---")
print(df_mulheres.head())

# 2. Quantas mulheres sobreviveram
mulheres_sobreviventes = df_mulheres[df_mulheres['Survived'] == 1]
num_mulheres_sobreviventes = mulheres_sobreviventes.shape[0]
print(f"\nNúmero de mulheres que sobreviveram: {num_mulheres_sobreviventes}")

# 3. Idade da pessoa mais velha
idade_maxima = df['Age'].max()
print(f"\nIdade da pessoa mais velha no navio: {idade_maxima} anos")

# 4. Idade média da Primeira Classe
df_classe1 = df[df['Pclass'] == 1]
media_idade_classe1 = df_classe1['Age'].mean()
print(f"\nIdade média dos passageiros da 1ª Classe: {media_idade_classe1:.2f} anos") # :.2f formata para 2 casas decimais"'"'"