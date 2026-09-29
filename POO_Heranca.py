# Classe Pai
class Veiculo:

    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self.ligado = False

    def ligar(self):
        self.ligado = True
        print(f"O {self.modelo} foi ligado.")

    def desligar(self):
        self.ligado = False
        print(f"O {self.modelo} foi desligado.")

# Classe Filho (Herda da Classe Veiculo)
class Carro(Veiculo):

    def __init__(self, marca, modelo, portas):
        super().__init__(marca, modelo)
        self.portas = portas

    def exibir(self):
        print(f"Carro: {self.marca} {self.modelo}, Portas: {self.portas}")

# Outra Classe Filho
class Moto(Veiculo):

    def __init__(self, marca, modelo, cilindradas):
        super().__init__(marca, modelo)
        self.cilindradas = cilindradas

    # Metodo unico na Classe Moto
    def empinar(self):
        print(f"A moto {self.modelo} está empinando.")

meu_carro = Carro("Volkswagen", "Golf", 4)
minha_moto = Moto("Honda", "CB 500", 500)

meu_carro.exibir()

meu_carro.ligar()

minha_moto.ligar()
minha_moto.empinar()
