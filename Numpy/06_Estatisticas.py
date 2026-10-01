import numpy as np

# Simulando as notas de 3 alunos em 4 provas
notas = np.array([
    [8.5, 7.0, 9.2, 6.5],
    [5.5, 6.8, 7.5, 8.0],
    [9.5, 9.0, 8.8, 10.0]
])

print("\nMatriz de Notas:\n")
print(notas)
print(type(notas))

# Agregações na matriz inteira
print(f"\nMedia geral da turma: {notas.mean():.2f}")
print(f"\nNota maxima da turma: {notas.max():.2f}")
print(f"\nNota minima da turma: {notas.min():.2f}")
print(f"\nSoma de todas as notas: {notas.sum():.2f}")

# Agregações por eixo (axis)
# Média de cada aluno (agregando nas colunas, axis = 1) arredondando para duas casas decimais
media_por_aluno = notas.mean(axis = 1).round(2)
print(f"\nMedia de cada aluno: {media_por_aluno}\n")

# Média de cada prova (agregando nas linhas, axis = 0) arredondando para duas casas decimais
media_por_prova = notas.mean(axis = 0).round(2)
print(f"\nMedia de cada prova: {media_por_prova}")