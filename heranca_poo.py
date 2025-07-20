class Veiculo:
    def __init__(self, cor, placa, numero_rodas):
        self.cor = cor
        self.placa = placa
        self.numero_rodas = numero_rodas

    def ligar_motor(self):
        print("Ligando o motor")



class Motocicleta(Veiculo):
    pass


class Carro(Veiculo):
    pass


class Caminhao(Veiculo):
    def esta_carregado(self):
        print("Não estou carregado")


moto = Motocicleta("preta", "abc-1234", 2)
moto.ligar_motor()

carro = Carro("branco", "xdej-0098", 4)
carro.ligar_motor()

caminhao = Caminhao("roxo", "gft_8712", 8)
caminhao.ligar_motor()