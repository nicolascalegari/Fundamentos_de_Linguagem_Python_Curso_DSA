import numpy as np

# Matriz 3x3
matriz = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])
print(type(matriz))
print(matriz.shape)

# Vetor 1D com 3 elementos
vetor = np.array([10, 20, 30])
print(type(vetor))
print(vetor.shape)

# Queremos somar os valores do vetor aos valores de CADA linha da matriz.
print(matriz)
print(vetor)

# Broadcasting: o vetor é "expandido" para cada linha da matriz
resultado = matriz + vetor
print("\nMatriz original:\n", matriz)
print("\nVetor:\n", vetor)
print("\nResultado com broadcasting:\n", resultado)

# Matriz com faturamento de 3 produtos em 4 meses
faturamento = np.array([
    [100, 110, 120, 130],
    [200, 210, 220, 230],
    [300, 310, 320, 330]
])

print(type(faturamento))
print(faturamento.shape)

# Vetor com um bônus (incentivo) para cada produto
bonus_por_produto = np.array([5, 10, 15])
print(type(bonus_por_produto))
print(bonus_por_produto.shape)

#Queremos adicionar um bônus a cada valor de faturamento, por linha. Ou seja, todos os itens da primeira linha devem receber o bônus de 5, por exemplo, e assim por diante.
# O NumPy "estica" (broadcast) o vetor bônus para que ele possa ser somado à matriz
# Mas forma de `bonus_por_produto` (3,) é incompatível com (3, 4)
# Para somar, precisamos que tenha a forma (3, 1) para o broadcast funcionar nas colunas
bonus_formatado = bonus_por_produto.reshape(3,1)
print(bonus_formatado.shape)

faturamento_com_bonus = faturamento + bonus_formatado
print("\nFaturamento com Bonus (via Broadcasting):\n")
print(faturamento_com_bonus)