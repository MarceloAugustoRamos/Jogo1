# Outra versao de como pode ser a batalha, comecando pelo bau, e continuando ate o final do boss


import random # IMPORTA DA BIBLIOTECA ALEATORIA
player = 100
boss = 100
ouro = 0

# INICIA AS VARIAVEIS PARA EXECUTAR NA BATALHA CONTRA O BOSS

espada = True
arco = True
machada = True

elmo = True
colete = True

print("Voce adentra uma sala meio escura...")
print("Voce encontra um baú e decide abrir ele")
print()  # QUALQUER PRINT VAZIO É PARA DAR ESPAÇO ENTRE OS TEXTOS NO TERMINAL


# acao = input("Aperte qualquer tecla para abrir o bau: ")
acao = input("Aperte qualquer letra para abrir o baú: ")

if acao == acao:

    bau = random.randint(1, 2)

    if bau == 1:

        # GERA NUMERO ALEATORIO PARA RECEBER ITEM ALEATORIO DO BAU
        itens = random.randint(1, 3)

        if itens == 1:
            ARMA = espada # ESPADA DA MAIS DANO QUE MACHADINHA
            item = "espada"
        elif itens == 2:  
            ARMA = arco  # ARCO RECEBE OUTROS PRINTS COM OUTRA HISTORIA
            item = "arco"
        else:
            ARMA = machada # MENOS DANO QUE ESPADA
            item = "machada"

        armadura = random.randint(1, 2)

        if armadura == 1:
            prot = elmo
            iten = "elmo" #REDUZ MENOS DANO QUE COLETE
        else:
            prot = colete
            iten = "colete" # REDUZ MAIS DANO CAUSADO PELO BOSS
            
        ganhos = random.randint(100, 250)
        ouro += ganhos

        print(f"Voce conseguiu: {item} e {iten}. Voce obteve {ouro} ouros.")


    # OPÇÃO CASO O BAU SEJA MIMICO 
    
    else:
        print("O baú se transformou em um mímico!!")
        print("Voce não tem outra opção senão lutar")

        acao = input("Digite 1 para dar um chute no mímico ou qualquer tecla para se esquivar e bater: ")

        if acao == "1":
            print("Voce dá um empurrão nele para trás")
            print()
            print("Voce matou o mímico, e agora pega os itens dele")
            kill = True
        else:
            print("Voce se esquiva dele e dá um soco nele por trás")
            print("Voce matou o mímico, e agora pega os itens dele")
            kill = True

        if kill == True:
            itens = random.randint(1, 3) # GERA NUMERO ALEATORIO PARA RECEBER ITEM ALEATORIO DO BAU

            if itens == 1:
                ARMA = espada # ESPADA DA MAIS DANO QUE MACHADINHA
                item = "espada"
            elif itens == 2:  
                ARMA = arco  # ARCO RECEBE OUTROS PRINTS COM OUTRA HISTORIA
                item = "arco"
            else:
                ARMA = machada # MENOS DANO QUE ESPADA
                item = "machada"

            armadura = random.randint(1, 2)

            if armadura == 1:
                prot = elmo
                iten = "elmo" #REDUZ MENOS DANO QUE COLETE
            else:
                prot = colete
                iten = "colete" # REDUZ MAIS DANO CAUSADO PELO BOSS
                
            ganhos = random.randint(100, 250)
            ouro += ganhos



        print(f"Voce matou ele e conseguiu: {item} e {iten}. Voce obteve {ouro} ouros.")



# INICIA A LUTA CONTRA O BOSS FINAL


print()
print("A proxima sala tem uma porta grande e com detalhes dourados...")
print("Voce não tem escolha a não ser encarar")

print()
acao = input("pressione qualquer letra para abrir a porta e entrar na sala... ")

if acao == acao:

    print("Voce inicia a batalha contra o boss!!")
    print()

    print("o boss esta vindo para cima de voce, o que voce faz?")
    acao = input("digite 1 para esquivar e contra atacar ou 2 para pular para tras: ")

    if acao == "1":

        if prot == elmo:
            playersofre = random.randint(6, 9)
            player -= playersofre
        else:
            playersofre = random.randint(1, 5)
            player -= playersofre

        if ARMA == espada:
            bosssofre = random.randint(20, 40)
            boss += bosssofre
        elif ARMA == machada:
            bosssofre = random.randint(10, 20)
            boss += bosssofre
        else:
            print("AAAA")
            
            
        print(f"Voce se esquivou do boss e contra atacou ele causando {playersofre} de dano, mas voce deu {bosssofre} de dano nele! ")
    else:
        print()
        print("Voce escolheu se esquivar e nao tomou dano")
        print()
        print("Voce esquivou para cima de pedra, e de cima dessa pedra voce pula com a espada na cabeça dele")

        bosssofre = random.randint(20, 40)
        boss += bosssofre
        print(f"Voce acerta a cabeça do boss em cheio com a espada, causando {bosssofre} de dano!")

    print("O demonio lança uma bola de fogo através de sua boca!")
    print()
    print("Voce vai esquivar e contra atacar pela latera, ou rebater com sua espada a devolver a bola de fogo?")

    acao = input("Digite 1 para esquivar e qualquer tecla para rebater: ")

    if acao == "1":
        print("Voce se esquivou dele e passou por de baixo dele")
        acao = input("Digite 1 para cortar as pernas do monstro ou qualquer tecla para bater na barriga dele com a espada! ")

        if acao == "1":
            print("Voce corta a perna dele e ele cai no chão, matando ele!")
        else:
            print("Voce enfia a espada na barriga dele e mata ele!")
            ganhos = random.randint(100, 250)
            ouro += ganhos
            print(f"Como recompensa por sua luta, voce ganha {ouro} ouros!")

    else:
        print("Voce decide rebater a bola de fogo")
        print("A bola de fogo acerta ele em cheio, matando ele")
        ganhos = random.randint(100, 250)
        ouro += ganhos
        print(f"Como recompensa por sua luta, voce ganha {ouro} ouros!")
