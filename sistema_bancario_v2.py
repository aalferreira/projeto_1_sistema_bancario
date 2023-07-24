# Potência Tech powered by iFood| Ciências de Dados com Python
# Desafio de projeto: Criando um Sistema bancário com Python


menu1 = """
Digite:
[1] Entrar na Conta
[2] Cadastrar Usuário
[3] Criar Conta
[4] Sair
"""

menu2 = """
Digite:

[5] Depósito
[6] Saque
[7] Extrato
[8] Voltar

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
usuarios = {}
conta = {}
num_conta = 1

while True:

    print(menu1)
    
    opcao = int(input())
    menu_control = True

    if opcao == 1:
        
        while menu_control:
            print(menu2)   

            opcao = int(input("\n Digite uma opção: \n"))

            if opcao == 5:
                deposito = float(input("\n Você selecionou a opção [5] Depósito. \n Por favor digite o valor que deseja depositar: \n "))

                def depositar(depositof, extratof, soma_depositof):

                    if depositof > 0:
                        extratof += depositof
                        soma_depositof += depositof
                        print(f" > > Depósito de R$ {depositof:.2f} feito com sucesso < <")
                        
                    else:
                        print("\n Valor inválido. Digite um valor positivo! \n")

                    return extratof, soma_depositof

                extrato, soma_deposito = depositar(deposito, extrato, soma_deposito)
                

            elif opcao == 6:
                saque = float(input(" \n Você selecionou a opção [6] Saque. \n Por favor digite o valor que deseja sacar: \n "))
                
                def sacar(saquef, extratof, soma_lim_saquef, LIMITE_SAQUEf, LIMITE_SAQUE_DIARIOf, soma_saquef):

                    if (saquef <= 0):
                        print (" \n ! ! Valor inválido. Insira uma valor maior que 0 ! ! \n")

                    elif (soma_lim_saquef <= (LIMITE_SAQUEf - 1)): 
                        valor_limite_saquef = LIMITE_SAQUE_DIARIOf - soma_saquef;
                        
                        if ((extratof - saquef) < 0):
                            print("\n Saldo Insuficiente. \n")

                        elif (valor_limite_saquef < saquef):
                            print (f"\n ! ! Você excedeu o valor limite diário de R${LIMITE_SAQUE_DIARIOf:.2f} ! !. \n Você pode sacar R${valor_limite_saquef:.2f} \n" )

                        else:
                            extratof -= saquef
                            soma_lim_saquef += 1
                            soma_saquef += saquef
                            print(f"\n > > Você sacou R$ {saquef:.2f} com sucesso < < \n")

                    else:
                        print (" \n ! ! Você excedeu a sua quantidade de saques diárias. Tente novamente amanhã ! ! \n")
                    
                    return extratof, soma_lim_saquef, soma_saquef
                
                extrato, soma_lim_saque, soma_saque = sacar(saque, extrato, soma_lim_saque, LIMITE_SAQUE, LIMITE_SAQUE_DIARIO, soma_saque)
                
            elif opcao == 7:

                def visualizar_extrato(soma_depositof, soma_saquef, soma_lim_saquef, extratof):
                    if soma_depositof == 0:
                        print("\n !! Não foram realizadas movimentações !! \n")

                    else:
                        print("\n Você selecionou a opção [7] Extrato. \n Segue abaixo o extrato da sua conta: \n")
                        print(f" \n Total em Depósitos: R$ {soma_depositof:.2f}")
                        print(f" \n Total em Saques: R$ {soma_saquef:.2f} ")
                        print(f" \n Quantidade de Saques realizados hoje: {soma_lim_saquef}")
                        print(f" \n Extrato: R$ {extratof:.2f}")

                visualizar_extrato(soma_deposito, soma_saque, soma_lim_saque, extrato)
            
            elif opcao == 8:
                menu_control = False

            else:
                print("\n ! ! Digite uma opção válida ! !")
 


    elif opcao == 2: ##  Criar usuário

        def criar_usuario(usuariosf):

            nome_cadastro  = input("\n Digite o seu nome por extenso: \n")
            data_nasc_cadastro = input("\n Digite o sua data de nascimento: \n")
            cpf_cadastro = input("\n Digite o seu CPF: \n")
            endereco_cadastro = input("\n Digite o seu endereco: \n ")

            if len(usuariosf) == 0:
                usuariosf = {
                    (cpf_cadastro): {"nome": nome_cadastro, "data_nasc":data_nasc_cadastro, "Endereco":endereco_cadastro}
                }
            elif cpf_cadastro not in usuariosf.keys():
                novo_usuario = {
                    (cpf_cadastro): {"nome": nome_cadastro, "data_nasc":data_nasc_cadastro, "Endereco":endereco_cadastro}
                    }
                usuariosf.update(novo_usuario)
            else:
                print("\n ! ! Usuário já cadastrado ! !")

            return usuariosf  
        
        copia_usuarios = usuarios.copy()
        usuarios = criar_usuario(copia_usuarios)
        print(usuarios)

    elif opcao == 3: ## Criar conta
        
        if usuarios == {}:
            print("\n ! ! Crie um usuário antes de criar a conta ! ! \n")
        else:

            def criar_conta(contaf, usuariosf, num_contaf):

                cpf_cadastro = input("\n Digite o seu CPF: \n")

                if len(contaf) == 0 and cpf_cadastro in usuariosf.keys():
                    num_contaf = 1
                    contaf = {
                        str(num_contaf): {"agencia": "0001", "usuario": usuariosf[cpf_cadastro]}
                    }
                    num_contaf += 1
                elif cpf_cadastro in usuariosf.keys():
                    nova_contaf = {
                        str(num_contaf): {"agencia": "0001", "usuario": usuariosf[cpf_cadastro]}
                        }
                    contaf.update(nova_contaf)
                    num_contaf += 1
                else:
                    print("\n ! ! Usuário não cadastrado ! !")

                return contaf, num_contaf
            
            copia_conta = conta.copy()
            copia_num_conta = num_conta
            conta, num_conta = criar_conta(copia_conta, usuarios, copia_num_conta)
            print(conta)



    elif opcao == 4:

        sair = int(input("\n Você deseja sair da sua conta? \n [1] Sim \t [2] Não \n:" ))

        if sair == 1:
            break

        elif sair == 2:
            print(f" \n Você retornou ao Menu inicial!")

        else:
            print("Opção Inválida. \n Digite [4] para SAIR e confirme com a opção [1] Sim \n")

    else:
        print(f" \n Opção Inválida. \n")