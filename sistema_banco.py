import datetime

#Espaço com as variaveis que vou usar com os seus respectivos nomes
saldo = 0.0
limite = 500.0
extrato = []
numero_saques = 0
limite_saques = 3

#Espaço com as variaveis de tratamento de repetição para o menu inicial
operacao_invalida="\nOperação inválido. Por favor, tente novamente.\n"
menu_inicial="Você séra redirecionado ao menu inicial, certifique-se de ter digitado a operação que deseja realizar corretamente."

def menu():
    print("\n========== BANCO VILAR S.A ===============")
    print("|-Escolha a melhor opçõa que lhe convem!-|")
    print("|-                                      -|")
    print("|-          *[1] Depositar              -|")
    print("|-          *[2] Sacar                  -|")
    print("|-          *[3] Extrato                -|")
    print("|-          *[4] Sair                   -|")
    print("|-                                      -|")
    print("|-                                      -|")
    print("==========================================\n")
    return input("Digite um numero de 1 a 4 para continuar: ").strip()

#Aqui o tratamento de caractere que eu nunca lembro de usar e espero que funcione em todo o sistema.
def input_valor_float(mensagem):
    while True:
        try:
            valor = float(input(mensagem).replace(",", "."))
            return valor
        except ValueError:
            print("Entrada inválida. Digite um valor numérico válido (use ponto ou vírgula para decimais).")

#Laço de repetição do menu. Com preguiça e falta de competencia de colocar time_sleep pq vou ter que pesquisar como usa e eu esqueci de importat o 'time' tbm
while True:
    opcao = menu()

    if opcao == "1":
        print("Você deseja fazer um deposito!")
        valor = float(input("Informe o valor do depósito que seja realizar: R$ "))
        if valor > 0:
            saldo += valor
            extrato.append(f"Deposito de R$ {valor:.2f}  {datetime.datetime.now()}")
            print(f"Parabéns o depósito de R$ {valor:.2f} foi realizado com sucesso.")
        else:
            print(f"{operacao_invalida}")
            print(f"{menu_inicial}")
            
#Poderia ter um time_sleep aqui  pelo menos de 2 segundos ou eu estou ficando louco ja        

    elif opcao == "2":
        if numero_saques >= limite_saques:
            print("Limite de saques diários atingido.")
            continue

        valor = float(input("Informe o valor do saque: R$ "))

        if valor <= 0:
            print("Valor inválido. Tente novamente.")
            print(f"{operacao_invalida}")
            print(f"{menu_inicial}")
        elif valor > limite:
            print(f"O valor máximo por saque é R$ {limite:.2f}.")
            print(f"{operacao_invalida}")
            print(f"{menu_inicial}")
        elif valor > saldo:
            print("Infelizmente seu saldo é insuficiente.")
            print(f"{operacao_invalida}")
            print(f"{menu_inicial}")
        else:
            saldo -= valor
            numero_saques += 1
            extrato.append(f"Saque de R$ {valor:.2f}  {datetime.datetime.now()}") #Esta bugado essa merda e eu não lembro pq, vou perguntar pro Alper pra ele me explicar
            print(f"Parabéns o saque de R$ {valor:.2f} foi realizado com sucesso.")
            
#Estou ficando louco memso

    elif opcao == "3":
        print("\n============== EXTRATO ==============")
        if not extrato:
            print("Nenhuma movimentação realizada.")
        else:
            for operacao in extrato:
                print(operacao)
        print(f"\nNo momento seu saldo atual é de: R$ {saldo:.2f}")
 
 #Ficou bem sem vergonha essa questão de depois de realizar a operação ir pro menu bem seco, mas se esta rodando não vou mudar agora que falta pouco (OBS:EU ACHO QUE FALTA POUCO)       

    elif opcao == "4":
        print("Encerrando o sistema. Obrigado por usar o BANCO VILAR S.A.!")
        break
    
#Cara eu detesto quando fecha o programa e o nome da pasta no final do terminal, preciso migrar pro tkinter logo e fugir do terminal

    else:
        print(f"{operacao_invalida}")
        print(f"{menu_inicial}")

#Se esta rodando esta bom, mas preciso arrumar o datatime.now que eu não entendi porque esta bugando ou na verdade eu não lembro(preciso de ajuda pra lembrar)

