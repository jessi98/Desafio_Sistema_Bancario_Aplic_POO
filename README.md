# 🏦 Sistema Bancário em Python com POO

Projeto desenvolvido durante o **Bootcamp de Back-End com Python** da [DIO (Digital Innovation One)](https://www.dio.me/), com foco em aplicar os princípios de **Programação Orientada a Objetos (POO)** em Python.

Este sistema simula um **banco digital**, permitindo operações como **criação de usuários e contas**, **depósitos**, **saques**, **emissão de extrato** e **controle de limite de saques**, tudo em ambiente de terminal.

---

## 📌 Objetivos

- Praticar conceitos fundamentais de POO:
  - Encapsulamento
  - Herança
  - Polimorfismo
  - Abstração
- Simular um sistema bancário funcional
- Aplicar boas práticas de organização de código em Python

---

## 🚀 Funcionalidades

- ✅ Cadastro de usuário (Pessoa Física)
- ✅ Criação de conta corrente vinculada ao CPF
- ✅ Depósito em conta
- ✅ Saque com limite de valor e quantidade
- ✅ Histórico de transações (extrato)
- ✅ Listagem de contas existentes
- ✅ Interface de menu via terminal

---

## 🧠 Conceitos OOP aplicados

- **Abstração**: com a classe abstrata `Transacao`
- **Herança**: `PessoaFisica` herda de `Cliente`, `ContaCorrente` herda de `Conta`
- **Encapsulamento**: uso de atributos protegidos (`_saldo`, `_cliente`, etc.)
- **Polimorfismo**: métodos `registrar()` sobrecarregados em `Deposito` e `Saque`

---

## 🛠️ Tecnologias e Ferramentas

- Python 3.11+
- Programação Orientada a Objetos
- Terminal/CLI
