################################################################################################
# regras para depósito:
# 1. apenas valores positivos
# 2. todos os depósitos devem ser armazenados em uma variável e exibidos na operação extrato
#
# regras para saque:
# 1. deve permitir apenas 3 operações de saque com limite de 500 por saque
# 2. deve exibir uma mensagem de saldo insuficiente caso não tenha saldo na conta
# 3. todos os saques devem ser armazenados em uma variável e exibidos na operação extrato
#
# regras para extrato:
# 1. deve listar todos os depósitos e saques realizados na conta
# 2. no final da listagem deve exibir o saldo atual da conta
# 3. se o extrato estiver em branco, exibir a mensagem 'Não foram realizadas movimentações.'
# 4. os valores devem ser exibidos utilizando o formato 'R$ xxx.xx'
################################################################################################

# construindo o menu de opções
menu = """

[1] Depósito
[2] Saque
[3] Extrato
[0] Sair

"""

# definindo as variáveis e constantes de acordo com as regras de negócio
saldo = 0
limite_por_operacao = 500
extrato = ""
saques_realizados = 0
LIMITE_SAQUES = 3

# laço de controle das operações
while True:

    # exibe o menu de opções
    opcao = input(menu)

    # tratamento da opção de depósito
    if opcao == "1":
        valor_deposito = float(input("Informe o valor do depósito: "))

        # verifica se o valor depositado é um inteiro positivo válido
        if valor_deposito <= 0:
            print("Valor de depósito inválido, por favor faça o depósito novamente.")
        else:
            # exibe o valor depositado e atualiza as variáveis
            print(f"Valor depositado: R$ {valor_deposito:.2f}")
            extrato += f'''Depósito: R$ {valor_deposito:.2f}\n'''
            saldo += valor_deposito

    # tratamento da opção de saque
    elif opcao == "2":
        valor_saque = float(input("Informe o valor do saque: "))

        # verifica se o valor sacado é um inteiro positivo válido
        if valor_saque <= 0:
            print("Valor de depósito inválido, por favor faça o saque novamente.")

        # verifica se o saldo é maior que 0 e se o valor sacado é menor ou igual ao saldo
        elif saldo > 0 and valor_saque <= saldo:
            #verifica o limite de operações diárias
            if saques_realizados == LIMITE_SAQUES:
                print("Não foi possível efetuar o saque: limite de operações diárias atingido.")
            # verifica se o valor do saque é maior que o limite permitido por operação
            elif valor_saque > limite_por_operacao:
                print(f"Não foi possível efetuar o saque: valor maior que limite por operação (R$ {limite_por_operacao:.2f}).")
            else:
                # exibe o valor sacado e atualiza as variáveis
                print(f"Saque efetuado: R$ {valor_saque:.2f}")
                extrato += f'''Saque: R$ {valor_saque:.2f}\n'''
                saques_realizados += 1
                saldo -= valor_saque
            
        else:
            print(f"Saldo insufuciente: R$ {saldo:.2f}")

    # tratamento da opção de extrato
    elif opcao == "3":
        # verifica se o extrato está vazio
        if len(extrato) == 0:
            print("Não foram realizadas movimentações.")

        else:
            # exibe o extrato e o saldo atual formatado
            print(extrato)
            print(f"Saldo atual: R$ {saldo:.2f}")
    
    # tratamento da opção de sair
    elif opcao == "0":
        print("Obrigado por utilizar nossos serviços.")
        break
    
    # tratamento das opções inválidas
    else:
        print("Operação inválida, por favor informe novamente a opção desejada.")