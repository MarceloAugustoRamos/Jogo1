vida = 3  #COMEÇA COM 3
pocao = 1  #COMEÇA COM 3

print("ATENÇÃO: CASO DIGITE UM NUMERO QUE NAO CORRESPONDE A DECISÃO, O CODIGO EXECUTARÁ COMO VERDADEIRO!!")
print()

print("Voce quer abrir o bau?")
print() #LINHA VAZIA ESPAÇO
x = input("Digite 1 para abrir, 2 para nao abrir: ") 

if x == "1": #SE QUISER ABRIR, EXECUTA A DECISAO ALEATORIA -- SENAO ELSE

    import random  #IMPORTA DA BIBLIOTECA ALEATORIA

    numero = random.randint(1, 2)  # GERA NUMERO ALEATORIO PARA A DECISAO DO BAÚ
    
    if numero == 1: #SE NUMERO 1 - GANHA POCAO --- SENAO ELSE
        print("voce ganhou uma poção e uma espada")
        espada = True
        pocao +=1 #ADICIONA UMA POÇÃO PARA A VARIAVEL
        
        print() #LINHA VAZIA ESPAÇO
        print(f"Voce possui {pocao} poções agora")

    else: #SE NAO FOR NUMERO 1 PERDE VIDA
        print("O baú era um mimico!")
        print("Voce nao pode fugir, então luta contra ele")
        
        bau = 100
        player = 100

        if pocao > 0:
            print(f"voce possui {pocao} poções, deseja usar para reviver?")
            
            revive = input("digite 1 para usar a poção e reviver, ou 2 para nao continuar: ") #OPÇÃO DE REVIVER OU NÃO

            if revive == "1":
                pocao -=1
                vida +=1
                print(f"Voce reviveu através da poção, agora possui {pocao} poções e {vida} vidas!")
                

            elif revive =="2":
                print("Voce escolheu nao reviver")
                
            else:
                print()
                print("Caracter invalido!! O codigo executará a proxima parte.")
        else:
            if vida == 0 and pocao == 0:
                print("Voce nao tinha poção para reviver, voce morreu.")
                exit()
            

else: #SENAO QUISER ABRIR O BAU, CONTINUA NORMALMENTE
    print("voce nao abre o bau")

print() #ESPAÇO
print("Voce sai dessa sala e vai para a sala a frente")

