# Definindo a classe (molde)
class Carro:

    # o metodo __init__ pe um construtor. Ele é chamado quando um novo objeto é criado
    # o self se refere a instancia do objeto que esta sendo criado
    def __init__(self, marca, modelo, ano):
        # Atributos (dados) do objeto
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.ligado = False # Um carro começa desligado por padrao

    # Metodos (comportamentos) do objeto
    def ligar(self):
        if not self.ligado:
            self.ligado = True
            print(f"O {self.modelo} esta ligado.")
        else:
            print(f"O {self.modelo} da estava ligado.")

    def desligar(self):
        if self.ligado:
            self.ligado = False
            print(f"O {self.modelo} foi desligado.")
        else:
            print(f"O {self.modelo} ja estava desligado.")

    def exibir_informacoes(self):
        print(f"Marca: {self.marca}, Modelo: {self.modelo}, Ano: {self.ano}")

# Criando objeto (instancia da classe Carro)
carro_1 = Carro ("Volkswagen", "Fusca", 1967)

# Usando os objetos
carro_1.ligar()
carro_1.desligar()

# Criando objeto (instancia da classe Carro)
carro_2 = Carro("Tesla", "Model S", 2025)

carro_2.exibir_informacoes()
carro_2.ligar()
