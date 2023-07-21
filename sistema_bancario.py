# Potência Tech powered by iFood| Ciências de Dados com Python
# Desafio de projeto: Criando um Sistema bancário com Python

menu = """
Digite:

[1] Depósito
[2] Saque
[3] Extrato
[4] Sair

"""

print(f" \n > > Bem-vindo(a) ao Banco DIO! < < \n")

deposito = 0
saque = 0
extrato = 0
LIMITE_SAQUE = 3
LIMITE_SAQUE_DIARIO = 500.0
soma_saque = 0
soma_deposito = 0
soma_lim_saque = 0

while True:

    print(menu)
    
    opcao = int(input())

    if opcao == 1:
        deposito = float(input("\n Você selecionou a opção [1] Depósito. \n Por favor digite o valor que deseja depositar: \n "))

        if deposito > 0:
            extrato += deposito
            soma_deposito += deposito
            print(f" > > Depósito de R$ {deposito:.2f} feito com sucesso < <")

        else:
            print("\n Valor inválido. Digite um valor positivo! \n")
            

    elif opcao == 2:
        saque = float(input(" \n Você selecionou a opção [2] Saque. \n Por favor digite o valor que deseja sacar: \n "))
        
        if (saque <= 0):
            print (" \n ! ! Valor inválido. Insira uma valor maior que 0 ! ! \n")

        elif (soma_lim_saque <= (LIMITE_SAQUE - 1)): 
            valor_limite_saque = LIMITE_SAQUE_DIARIO - soma_saque;
            
            if ((extrato - saque) < 0):
                print("\n Saldo Insuficiente. \n")

            elif (valor_limite_saque < saque):
                print (f"\n ! ! Você excedeu o valor limite diário de R${LIMITE_SAQUE_DIARIO:.2f} ! !. \n Você pode sacar R${valor_limite_saque:.2f} \n" )

            else:
                extrato -= saque
                soma_lim_saque += 1
                soma_saque += saque
                print(f"\n > > Você sacou R$ {saque:.2f} com sucesso < < \n")

        else:
            print (" \n ! ! Você excedeu a sua quantidade de saques diárias. Tente novamente amanhã ! ! \n")

    elif opcao == 3:

        if soma_deposito == 0:
            print("\n !! Não foram realizadas movimentações !! \n")

        else:
            print("\n Você selecionou a opção [3] Extrato. \n Segue abaixo o extrato da sua conta: \n")
            print(f" \n Total em Depósitos: R$ {soma_deposito:.2f}")
            print(f" \n Total em Saques: R$ {soma_saque:.2f} ")
            print(f" \n Quantidade de Saques realizados hoje: {soma_lim_saque}")
            print(f" \n Extrato: R$ {extrato:.2f}")
       
    elif opcao == 4:

        sair = int(input("\n Você deseja sair da sua conta? \n [1] Sim \t [2] Não \n:" ))

        if sair == 1:
            break

        elif sair == 2:
            print(f" \n Você retornou ao Menu inicial! {menu}")

        else:
            print("Opção Inválida. \n Digite [4] para SAIR e confirme com a opção [1] Sim \n")

    else:
        print(f" \n Opção Inválida. \n")