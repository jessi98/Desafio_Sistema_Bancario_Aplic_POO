class Bicicleta:
    def __init__(self, cor, modelo, ano, valor):
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.valor = valor

    def buzinar(self):
        print(("Plim plim..."))

    def parar(self):
        print("Parando bicicleta...")
        print("Bicicleta parada!")

    def correr(self):
        print("Vrummmm...")

    # def __str__(self):
    #     return f"Bicicleta: cor={self.cor}, modelo={self.modelo}, ano={self.ano}, valor={self.valor}"

    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"
        # atributos = '\n'.join([f'{chave} = {valor}' for chave, valor in self.__dict__.items()])
        # return f"{self.__class__.__name__}:\n{atributos}"

b1 = Bicicleta("vermelha", "caloi", 2022, 600)
b1.buzinar()
b1.parar()
b1.correr()
print(b1.cor, b1.modelo, b1.ano, b1.valor)
print(b1)