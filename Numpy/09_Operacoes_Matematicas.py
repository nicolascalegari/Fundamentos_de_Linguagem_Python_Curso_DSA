import numpy as np

# Criando duas matrizes
A = np.array([[1,2],[3,4]])
B = np.array([[5,6],[7,8]])

# Produto de Matrizes (diferente da multiplicação elemento a elemento)
# Usando o operador @
produto_matricial = A @ B
print(f"\nProduto de A por B:\n\n{produto_matricial}\n")

# Nesse trecho acima, são criadas duas matrizes 2×2 chamadas A e B. Em seguida, é realizado o produto matricial entre elas 
# usando o operador @. Diferente da multiplicação elemento a elemento (que faz a operação posição por posição), o produto 
# matricial segue as regras da álgebra linear: cada elemento da matriz resultante é obtido multiplicando os elementos de uma 
# linha da primeira matriz pelos elementos de uma coluna da segunda e somando esses produtos. O cálculo do produto é:

# [ [1 * 5 + 2 * 7, 1 * 6 + 2 * 8], [3 * 5 + 4 * 7, 3 * 6 + 4 * 8] ] = [[19, 22], [43, 50]]

# Usando np.dot() ao invés de @
produto_matricial = np.dot(A, B)
print(f"Produto de A por B:\n{produto_matricial}\n")

print(f"\nMatriz A:\n{A}\n")
print(f"Matriz B:\n{B}\n")

# Criando duas matrizes 2x2
A = np.array([[10,20],[30,40]])
B = np.array([[7,14],[4,3]])

# Soma de matrizes
soma = A + B

# Subtração de matrizes
subtracao = A - B

# Divisão elemento a elemento
divisao = A / B

print("Matriz A:\n", A)
print("\nMatriz B:\n", B)
print("\nSoma A + B:\n", soma)
print("\nSubtracao A - B:\n", subtracao)
print("\nDivisao A / B:\n", divisao)
