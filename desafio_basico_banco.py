menu = """

    [d]-Deposito
    [s]-Sacar
    [e]-Extrato
    [q]-Sair


=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)
   

    if(opcao == 'd'):
        print("Sacar...")

        valor = float(input("Digite o valor do saque:"))
        if(valor > 0):
            saldo += valor
            extrato += f"Depósito: R$ {valor:2f}\n"
        else:
            print("Operação falhou o valor informado é inválido.")      

    elif(opcao == 's'):
        valor = float(input("Informe o valor do saque: "))
        
        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Saldo insuficiente!")
        
        elif excedeu_limite:
            print("Excedeu limite!")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1
    
    elif(opcao == 'e'):
        print("==============EXTRATO=============")
        print("Não foram realizados movimentações," if not extrato else extrato)
        print(f"\n Saldo: R${saldo:.2f}")
        print("==================================")

    elif(opcao == 'q'):
        break

    else:
        print("Opção inválida, por favor selecionar novamente a opreção correta!")
        