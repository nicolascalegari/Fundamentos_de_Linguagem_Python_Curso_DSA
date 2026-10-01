import numpy as np

# Simulando dados de preços de produtos
precos = np.array([19.99, 25.50, 8.90, 43.00])
print(f"\nPrecos originais: {precos}\n")

# Aplicando um desconto de 10% a todos os preços de uma vez
precos_com_desconto = precos * 0.90
print(f"\nPrecos com 10% de desconto: {precos_com_desconto}\n")

# Mesmo resultado da célula anterior usando Python puro
# Lista original de preços
precos_pp = [19.99, 25.50, 8.90, 43.00]
# Aplicando desconto de 10% usando list comprehension
precos_com_desconto_pp = [preco * 0.90 for preco in precos_pp]
print(f"\nPrecos com 10% de desconto: {precos_com_desconto_pp}\n")

# Adicionando um valor fixo de frete
precos_finais = precos_com_desconto + 5.00
print(f"\nPrecos finais com frete: {precos_finais}\n")

# Usando funções universais (ufuncs) do NumPy
# Exemplo: calculando a raiz quadrada de cada elemento
raizes = np.sqrt(precos)
print(f"\nRaiz quadrada dos precos: {raizes}")