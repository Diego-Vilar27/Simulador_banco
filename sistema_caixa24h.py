#Eu acho que faltou você colocar o cartão e senha, mas ninguem viu então continue e se divirta

#Mais uma tela de DOS pra vida sem vergonha com (=, | e -).Vou meter ate um AD no canto pra valorizar.
def menu():
    print("\n === BEM VINDO AO CAIXA ELETRONICO DO BANCO VILAR S.A. ====")
    print("|-                                                        -|")
    print("|-   Menu do Caixa 24horas      ________________________  -|")
    print("|-                             |Em caso de duvidas:     | -|")
    print("|-     1 - Depositar           |Ligue no nosso 0800-1010| -|")
    print("|-     2 - Sacar               |Atendimento 24/7.       | -|")
    print("|-     3 - Sair                 ------------------------  -|")
    print("|-                                                        -|")
    print(" ==========================================================\n")
    return input("Escolha uma opção: ")

# Eu poderia ter feito a variavel antes, mas esse tem poucas e nem vou perder tanto tempo com isso
#Quem me dera ter dinheiro no banco :(
saldo = 1000.00

#Laço de repetição padrãozinho que é oque eu decorei então tem que gastar ela ate aprender uma melhor
while True:
    opcao = menu()

    if opcao == "1":
        valor = float(input("Informe o valor para depósito: R$ "))
        if valor > 0:
            saldo += valor
            print(f"Depósito de R$ {valor:.2f} realizado com sucesso.")
            print(f"Saldo atual: R$ {saldo:.2f}")
            print("Você sera direcionado ao menu inicial")
        else:
            print("Valor inválido. Tente novamente.")

    elif opcao == "2":
        valor = float(input("Informe o valor para saque: R$ "))
        if valor <= 0:
            print("Valor inválido.")
        elif valor > saldo:
            print("Saldo insuficiente para esse saque.")
        else:
            saldo -= valor
            print(f"Saque de R$ {valor:.2f} realizado com sucesso.")
            print(f"Saldo atual: R$ {saldo:.2f}")

    elif opcao == "3":
        print("Encerrando o programa. Obrigado por usar o caixa eletrônico!")
        break

    else:
        print("Opção inválida. Por favor, escolha 1, 2 ou 3.")
        
#Agora so mandar curriculo no ITAU, Bradesco, Nubank e todas as outras. Lembrando se robou não mexe
