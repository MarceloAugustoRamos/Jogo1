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


# LUTA CONTRA O BOSS


ouro = 0
player = 100
boss = 100 
vida = 3
turno = 0

print("Voce adentra uma sala que tem um boss")
print("Caso derrote o boss, ganhará ouro")
print()
print("Voce quer lutar contra ele? ")

decisao = input("digite 1 para lutar, e qualquer outro botao para nao lutar: ")

if decisao == "1":
    print("Voce decide lutar contra ele!")

    print("Voce se depara com o demonio!")
    while player >0 and boss >0:

        while vida >0:
        
        
        
            acao = input("Aperte 1 para dar o ataque no boss! ") #ATAQUE 
            print()
            
            if acao == "1":
                
                import random
                dano = random.randint(15, 30)  
                boss -= dano
                turno +=1

                if boss <=0:
                    print(f"voce deu {dano} de dano no boss e matou ele!") 
                    
                    ganho = random.randint(100, 250)
                    ouro += ganho  # GANHOS DE RECOMPENSA PELO KILL DO BOSS
                    print(f"Voce ganhou {ouro} ouros como recompensa!")
                    break

                else:
                    print(f"(TURNO {turno}) Voce deu {dano} de dano no boss, agora ele tem {boss} de hp") # DANO DO TURNO DO JOGADOR

                if boss >0:    

                
                    if player >0:
                        print()
                        print("agora é o turno do boss!")
                        print()
                        dano = random.randint(15, 30)  # DANO DO TURNO DO BOSS
                        player -= dano

                        if player <=0:
                            print(f"voce tomou {dano} de dano e morreu!")
                            vida -=1
                            print(f"Voce perdeu uma vida e agora {vida} vidas. a batalha vai recomeçar")
                            print()
                        else:
                            print(f"(TURNO {turno}) Voce tomou {dano} de dano do boss, agora voce tem {player} de HP!") 
                            print()
   
else:
    print("Voce decide nao lutar contra o boss")

print("Voce entra em outra sala.")