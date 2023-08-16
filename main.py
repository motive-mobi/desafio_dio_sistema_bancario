menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair
--------------------
[u] Cadastra usuário
[c] Cadastra conta

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3
AGENCIA = "0001"
numero_conta = 1
usuarios = list()
contas = list()

def atualiza_saldo(saldo_atual, operacao):
    global saldo
    global extrato
    global numero_saques

    if operacao == "saque":
        saldo -= saldo_atual
        extrato += f"Saque: R$ {saldo_atual:.2f}\n"
        numero_saques += 1

    elif operacao == "deposito":
        saldo += saldo_atual
        extrato += f"Depósito: R$ {saldo_atual:.2f}\n"

    else:
        print("Operação inválida.")

def executa_extrato(saldo, /, extrato):
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if extrato == "" else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==========================================")

def executa_saque(saldo, valor, extrato, limite, numero_saques, limite_saques):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= LIMITE_SAQUES

    if excedeu_saldo:
        print("Operação falhou! Você não tem saldo suficiente.")

    elif excedeu_limite:
        print("Operação falhou! O valor do saque excede o limite.")

    elif excedeu_saques:
        print("Operação falhou! Número máximo de saques excedido.")

    elif valor > 0:
        atualiza_saldo(valor, "saque")

    else:
        print("Operação falhou! O valor informado é inválido.")

def executa_deposito(saldo, valor, extrato):
    if valor > 0:
        atualiza_saldo(valor, "deposito")

    else:
        print("Operação falhou! O valor informado é inválido.")

def verifica_cpf(numero):
    cpf_buscado = numero

    for valor in usuarios:
        if valor[0] == cpf_buscado:
            return valor

def cadastra_usuario():
    cpf = str(input("Informe o CPF: "))
    cpf = cpf.replace('.', '')
    cpf = cpf.replace('-', '')

    if not verifica_cpf(cpf):
        nome = str(input("Informe o nome: "))
        data_nascimento = str(input("Informe a data de nascimento: "))
        endereco = str(input("Informe o endereço: "))
        usuarios.append([cpf, nome, data_nascimento, endereco])
    else:
        print(f"CPF já cadastrado: {cpf}")

def cadastra_conta(agencia, cliente, conta):
    global numero_conta
    contas.append([agencia, cliente, conta])
    numero_conta += 1
    print(f"Clientes: {usuarios}")
    print(f"Contas: {contas}")

while True:

    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Informe o valor do depósito: "))
        executa_deposito(saldo, valor, extrato)

    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))
        executa_saque(saldo=saldo, valor=valor, extrato=extrato, limite=limite, numero_saques=numero_saques, limite_saques=LIMITE_SAQUES)

    elif opcao == "e":
        executa_extrato(saldo, extrato=extrato)

    elif opcao == "u":
        cadastra_usuario()

    elif opcao == "c":
        cpf = str(input("Informe o CPF do cliente: "))
        if verifica_cpf(cpf):
            user = verifica_cpf(cpf)
            cadastra_conta(AGENCIA, user, numero_conta)
            print("Conta cadastrada com sucesso!")
        else:
            print("Cliente não encontrado!")

    elif opcao == "q":
        print("Obrigado por utilizar nossos serviços!")
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
