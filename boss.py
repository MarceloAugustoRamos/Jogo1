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