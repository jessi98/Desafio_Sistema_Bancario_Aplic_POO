# 🏦 Sistema Bancário Simples - Etapa 3 (POO)

Este projeto foi construído durante o **Bootcamp Backend com Python da DIO**.

---

## Principais Melhorias e Mudanças

- **Classes e objetos** para representar clientes, contas, transações e histórico:
  - `Cliente` (base), `PessoaFisica` (herança para clientes pessoa física)
  - `Conta` (base), `ContaCorrente` (especialização da conta)
  - `Transacao` (classe abstrata), e suas implementações `Deposito` e `Saque`
  - `Historico` para armazenar o registro de transações

- **Encapsulamento** de dados da conta (`_saldo`, `_numero`, `_agencia`, etc.) para proteger o estado interno.
- **Herança** para reutilizar código em classes filhas.
- **Abstração** com a classe abstrata `Transacao` e método `registrar()` para uniformizar as operações financeiras.
- **Registros de transações** com data e hora na classe `Historico`.
- **Separação clara de responsabilidades**, onde:
  - Cliente gerencia contas,
  - Conta gerencia saldo e operações,
  - Transação gerencia o registro da operação.

---

## Funcionalidades man
