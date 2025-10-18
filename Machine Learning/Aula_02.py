# Crie uma matriz NumPy chamada dados_vendas de 4 linhas e 3 colunas (4x3) contendo os seguintes dados.

import numpy as np

dados_vendas = np.array([[150, 200, 250], 
                        [140, 220, 260],
                        [160, 210, 270],
                        [145, 190, 240]])

print("Matriz de Vendas (USD):\n", dados_vendas)

tx_conversao = 5.15
vendas_em_reais = dados_vendas * tx_conversao

print("\nMatriz de Vendas (BRL):\n", vendas_em_reais)

total_por_produto = np.sum(vendas_em_reais, axis=0) # axis=0 significa "ao longo do eixo 0" (linhas) 
print("\nTotal de vendas por produto (A, B, C):", total_por_produto)

vendas_semana_3 = vendas_em_reais[2, :] # Linha de índice 2, todas as colunas
print("\nVendas da Semana 3:", vendas_semana_3)