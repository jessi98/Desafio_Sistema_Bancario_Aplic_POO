from datetime import datetime
import textwrap
from abc import ABC, abstractmethod

class Cliente:
    def __init__(self, endereco):
        self.endereco = endereco
        self.contas = []

    def realigar_transacao(self, conta, transacao):
        transacao.registrar(conta)

    def adicionar_conta(self, conta):
        self.contas.append(conta)

class PessoaFisica(Cliente):
    def __init__(self, nome, data_nascimento, cpf, endereco):
        super().__init__(endereco)
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.cpf = cpf

class Transacao(ABC):
    def registrar(self, conta):
        pass

class Historico:
    def __init__(self):
        self.transacao = []

    def adicionar_transacao(self, descricao):
        data_hora = datetime.now().strftime('%d/%m/%Y %H:%M:%S')
        registro = f"[{data_hora}] {descricao}"
        self.transacao.append(registro)

class Conta:
    def __init__(self, numero, agencia, Cliente, saldo=0.00):
        self._numero = numero
        self._agencia = agencia
        self._cliente = Cliente
        self._historico = Historico()
        self._saldo = saldo
        self.limite = 500
        self.numero_saques = 0
        self.LIMITE_SAQUES = 3


    def mostra_saldo(self):
        return self._saldo

    @classmethod
    def nova_conta(cls, Cliente, numero):
        return cls(Cliente=Cliente, numero=numero)


    def sacar(self, valor):
        if valor > self._saldo or self._saldo == 0:
            print(f"Não foi possível realizar o saque de R${valor:.2f}, seu saldo atual é insuficiente.")
            return False

        elif valor > self.limite:
            print(f"Você atingiu o limite de saques.")
            return False

        elif self.numero_saques >= self.LIMITE_SAQUES:
            print("Você já atingiu o limite de saques por hoje.")
            return False

        else:
            self._saldo -= valor
            self.numero_saques += 1
            print(f"Saque de R$ {valor:.2f}, realizado com sucesso!")
        return True


    def depositar(self, valor):
        if valor > 0:
            self._saldo += valor
            print("Depósito realizado com sucesso.")
            return True
        else:
            print("Valor inválido para depósito.")
            return False

class ContaCorrente(Conta):
    def __init__(self, numero, agencia, Cliente, saldo=0.0, limite=500, LIMITE_SAQUES=3):
        super().__init__(numero, agencia, Cliente, saldo)
        self.limite = limite
        self.LIMITE_SAQUES = LIMITE_SAQUES

class Deposito(Transacao):
    def __init__(self, valor):
        self.valor = valor

    def registrar(self, conta):
        sucesso=conta.depositar(self.valor)
        if sucesso:
            conta._historico.adicionar_transacao(f"Depósito: R${self.valor:.2f}\n")

class Saque(Transacao):
    def __init__(self, valor):
        self.valor = valor

    def registrar(self, conta):
        sucesso = conta.sacar(self.valor)
        if sucesso:
            conta._historico.adicionar_transacao(f"Saque: R${self.valor:.2f}\n")

def criar_usuario (usuarios):
    cpf = input("Informe o CPF (somente número): ")
    usuario = filtrar_usuarios(cpf, usuarios)

    if usuario:
        print("Usuário já cadastrado com esse CPF. ")
        return

    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (Logradouro, nro - bairro - cidade/sigla estado): ")

    novo_usuario = {
        "nome": nome,
        "data_nascimento": data_nascimento,
        "cpf": cpf,
        "endereco": endereco
    }

    usuarios.append(novo_usuario)
    print("Usuário criado com sucesso!")
    return novo_usuario

def filtrar_usuarios(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None


def criar_cc (agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrar_usuarios(cpf, usuarios)

    if usuario:
        nova_conta = ContaCorrente(numero=numero_conta, agencia=agencia, Cliente=usuario)
        print("Conta criada com sucesso")
        return nova_conta
    print("Usuario não encontrado, fluxo de criação de conta encerrado!")
    return None


def listar_contas(contas):
    for conta in contas:
        linha = f"""\
        Agência:\t{conta._agencia}
        C/C:\t{conta._numero}
        Titular:\t{conta._cliente["nome"]}"""
        print("=" * 40)
        print(linha)

def menu():
    menu = """\n
    ==========MENU==========
    O que deseja fazer hoje?

    [1] Depositar
    [2] Sacar
    [3] Extrato
    [4] Nova Conta
    [5] Listar Contas
    [6] Novo Usuario
    [0] Sair

    => """
    return input(textwrap.dedent(menu))

def main():
    usuarios = []
    contas = []

    while True:
        opcao = menu()

        if opcao == '1':
            cpf = input("CPF do titular: ")
            usuario = filtrar_usuarios(cpf, usuarios)

            if not usuario:
                print("Usuário não encontrado.")
                continue

            conta = next((conta for conta in contas if conta["usuario"]["cpf"] == cpf), None)
            if not conta:
                print("Conta não encontrada.")
                continue

            valor = float(input("Valor do depósito: R$ "))
            deposito = Deposito(valor)
            deposito.registrar(conta)

        elif opcao == '2':
            cpf = input("CPF do titular: ")
            usuario = filtrar_usuarios(cpf, usuarios)

            if not usuario:
                print("Usuário não encontrado.")
                continue

            conta = next((conta for conta in contas if conta["usuario"]["cpf"] == cpf), None)
            if not conta:
                print("Conta não encontrada.")
                continue

            valor = float(input("Valor do saque: R$ "))
            saque = Saque(valor)
            saque.registrar(conta)

        elif opcao == '3':
            cpf = input("CPF do titular: ")
            usuario = filtrar_usuarios(cpf, usuarios)

            if not usuario:
                print("Usuário não encontrado.")
                continue

            conta = next((conta for conta in contas if conta["usuario"]["cpf"] == cpf), None)
            if not conta:
                print("Conta não encontrada.")
                continue

            print("\n=== EXTRATO ===")
            for transacao in conta._historico.transacao:
                print(transacao)
            print(f"Saldo atual: R${conta._saldo:.2f}")

        elif opcao == '4':
            numero_conta = len(contas) + 1
            conta = criar_cc(agencia='0001', numero_conta=numero_conta, usuarios=usuarios)

            if conta:
                contas.append(conta)

        elif opcao == '5':
            listar_contas(contas)

        elif opcao == '6':
            criar_usuario(usuarios)

        elif opcao == '0':
            break

        else:
            print("Operação inválida, tente novamente.")

main()