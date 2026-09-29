class Veiculo:

    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def exibir(self):
        print(f"Veiculo generico: {self.marca} {self.modelo}")

class Carro(Veiculo):

    def __init__(self, marca, modelo, portas):
        super().__init__(marca, modelo)
        self.portas = portas

    # Sobrescrevendo o metodo da classe pai
    def exibir(self):
        print(f"Carro: {self.marca} {self.modelo} | Portas: {self.portas}")

class Moto(Veiculo):

    def __init__(self, marca, modelo, cilindradas):
        super().__init__(marca, modelo)        
        self.cilindradas = cilindradas

    def exibir(self):
        print(f"Moto: {self.marca} {self.modelo} | Cilindradas: {self.cilindradas}cc")

# Lista de veiculos de diferentes tipos
veiculos = {
    Carro("Toyota", "Corolla", 4),
    Moto("Yamaha", "MT-07", 700),
    Veiculo("Caloi", "Ceci") # Usando a classe pai diretamente
}

# O mesmo objeto se comporta de forma diferente para cada objeto
for v in veiculos:
    v.exibir()