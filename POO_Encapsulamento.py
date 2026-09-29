class Carro:

    # Metodo construtor
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self._velocidade = 0 # Atributo protegido
        self.__horsepower = 300 # Atributo privado

    # Metodo getter para obter valor da velocidade
    def get_velocidade(self):
        return self._velocidade

    # Metodo setter para alterar o valor da velocidade
    def acelerar(self, valor):
        if valor > 0:
            self._velocidade += valor
            print(f"O {self.modelo} acelerou para {self._velocidade} km/h.")
        else:
            print("O valor de aceleração deve ser positivo.")

    # Metodo geral
    def frear(self, valor):
        if valor > 0:
            self._velocidade -= valor
            if self._velocidade < 0:
                self._velocidade = 0
            print(f"O {self.modelo} freou para {self._velocidade} km/h.")
        else:
            print("O valor de frenagem deve ser positivo.")

# Cria a instancia da class
carro_encapsulado = Carro("Hyundai", "HB20", 2026)

# Observe que o atributo _velocidade nao aparece na lista (No VSCode aparece)
carro_encapsulado.ano

# Interagindo com o objeto atraves de metodos
carro_encapsulado.acelerar(50)
print(f"Velocidade atual: {carro_encapsulado.get_velocidade()} km/h")
carro_encapsulado.frear(20)
print(f"Velocidade atual: {carro_encapsulado.get_velocidade()} km/h")

# Acessar atributo protegido
print(carro_encapsulado._velocidade)

# Acesso direto (nao recomendado)
carro_encapsulado._velocidade = 200 # Quebra o encapsulamento
print(f"Velocidade alterada diretamente: {carro_encapsulado._velocidade} km/h")

# Tentativa de acesso direto falha
try:
    print(carro_encapsulado.__horsepower)
except AttributeError as e:
    print("Erro ao acessar diretamente:", e)

# O atributo existe so que com nome interno modificado
print("Acessando pelo nome real interno:", carro_encapsulado._Carro__horsepower)

# Acesso direto (nao recomendado)
carro_encapsulado.__horsepower = 350 # Isso quebra o encapsulamento
print(f"Horsepower alterado diretamente: {carro_encapsulado.__horsepower}")

# _atributo → apenas convenção, acesso é permitido.

# __atributo → Python aplica name mangling, mudando o 
# nome interno do atributo para _NomeDaClasse__atributo. 
# Isso dificulta o acesso, mas ainda é possível se você souber o nome interno.
