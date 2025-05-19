#início
print('Você é preso em uma masmorra, e perdeu suas memórias')
print('A única coisa em que pensa é: ESCAPAR')
print('')
#Equipamento inicial
print('Você começa com uma espada com 3 de durabilidade e uma poção de retorno, que ao entrar em situções de perigo, é consumida para retornar à primeira sala')
print('ao digitar algo que não aparece nas opções, a última será escolhida')
print('Digite apenas números')
print('')
espada = 3
pocao = 1
vida = True
chave = 0

# Variáveis das salas na primeira parte da masmorra
tranca3 = True #tranca da porta vermelha na sala 3
prim3 = True #verifica se é a primeira vez que o jogador entrou na sala 3(para pegar a chave)
prim4 = True #verifica se é a primeira vez que o jogador entrou na sala 4(para pegar a poção)
prim6 = True #verifica se é a primeira vez que o jogador entrou na sala 6(para pegar a chave)
skl5 = True  #verifica se o esqueleto na sala 5 não foi derrotado
sala7 = False #verifica se o jogador chegou na sala 7

while vida:
    #Sala 1
    print('Você vê 3 portas')
    print('1: Frente')
    print('2: Esquerda')
    print('3: Direita')
    porta = int(input('> '))

    if porta == 1:
        #Armadilha
        print('Você cai em uma armadilha')
        if pocao > 0:
            print('Você bebe uma poção de retorno e sobrevive, retornando à primeira sala.')
            pocao -= 1
        else:
            print('Você morreu.')
            vida = False

    elif porta == 2:
        #Sala 2
        print('essa sala está vazia, você vê duas portas.')
        print('1: A frente')
        print('2: Direita')
        porta2 = int(input('> '))

        if porta2 == 1:
            #Sala 6
            if prim6:
                print('Você vê uma chave pendurada em uma das paredes.')
                print('Você pega a chave.')
                prim6 = False
            print('Essa sala tem apenas uma porta.')
            print('1: Em frente')
            int(input('> '))
            sala7 = True
        
        else:
            sala7 = True


    else:
        #Sala 3

        if prim3:
            print('Nessa sala, você vê uma mesa com uma chave em cima.')
            print('Você pega a chave.')
            chave += 1
            prim3 = False

        #estrutura de repetição que repete a sala 3 caso o jogador não tenha uma chave e tente abrir a tranca
        tranca3W = True
        while tranca3W:
            print('Há duas portas nessa sala.')
            if tranca3:
                print('1: Porta vermelha que está trancada(1 chave).')
            else:
                print('1: Porta vermelha')
            print('2: Porta verde')
            porta3 = int(input('> '))
    
            if tranca3 == True and porta3 == 1 and chave > 0:
                print('Você usa uma chave e destranca a porta vermelha')
                tranca3 = False
                tranca3W = False
            elif porta3 == 1 and chave == 0:
                print('Chaves insuficientes')
            
            else:
                tranca3W = False


            if porta3 == 2:
                #sala 5
                if skl5:
                    print('Você encontra um esqueleto hostil nessa sala')
                    print('Será necessário 1 de durabilidade da espada para derrotar')
                    print(f'Sua espada tem {espada} de durabilidade')
                    print('1: Lutar')
                    input('> ')
                    if espada > 0:
                        print('Você derrota o esqueleto com sucesso')
                        espada -= 1
                        skl5 = False
                    else:
                        print('Sua espada quebra na luta e você fica indefeso')
                        if pocao > 0:
                            print('Você bebe uma poção de retorno e sobrevive, retornando à primeira sala')
                            pocao -= 1
                        else:
                            print('Você morreu')
                            vida = False

                    print('Essa sala tem apenas uma porta')
                    print('1: Em frente')
                    porta3 = 1 #faz com que o jogador entre na sala 4

            
            elif porta3 == 1:

                #Sala 4
                if prim4:
                    print('Nessa sala, você encontra um laboratório de alquimia com vários tipos de equipamentos.')
                    print('A maioria está quebrado e inutilizável, mas no meio dos destroços, você encontra uma poção de retorno.')
                    pocao += 1
                    prim4 = False
                print('Essa sala tem apenas uma porta')
                print('1: Em frente')
                int(input('> '))
                tranca = False #desativa a tranca na porta vermelha(entrando em outro lugar)
                sala7 = True

    if sala7:
        print('A próxima sala é um checkpoint.')
        print('Se você continuar, não terá mais a chance de voltar para essa parte da masmorra')
        print('1: Continuar')
        print('2: Voltar para a primeira sala(utiliza uma poção de retorno)')
        parte2 = int(input('> '))
        if parte2 == 1:
            break #encerra a estrutura de repeitção da primeira parte caso o jogador chege na sala 7
        elif parte2 == 2 and pocao == 0:
            print('Você não tem nenhuma poção e segue em frente para a próxima sala')
            break #encerra a estrutura de repeitção da primeira parte caso o jogador chege na sala 7
        elif parte2 == 2 and pocao > 0:
            pocao -= 1
            

# Variáveis das salas na segunda parte da masmorra
prim7 = True #verifica se é a primeira vez que o jogador entrou na sala 7(para acender a fogueira)
tranca7 = True #tranca da porta a direita na sala 7
prim8 = True #verifica se é a primeira vez que o jogador entrou na sala 8(para pegar a espada grande)
tranca8 = True #tranca da porta demoníaca na sala 8
dem11 = True #verifica se o demônio na sala 11 não foi derrotado
prim9 = True #verifica se é a primeira vez que o jogador entrou na sala 9(para pegar a poção)
porta10 = 0
cac13 = True

while vida:
    #Sala 7
    #estrutura de repetição que repete a sala 7 caso o jogador não tenha uma chave e tente abrir a tranca
    tranca7W = True
    while tranca7W:
        if prim7:
            print('Ao chegar nessa sala você encontra uma fogueira.')
            print('Você acende a fogueira e descansa por um momento')
            print('Suas poções de retorno agora iram te teleportar a essa sala.')
            prim7 = False
        
        print('Nessa sala você vê 3 portas.')
        if tranca7:
            print('1: Porta a direita, que está trancada(1 chave)')
        else:
            print('1: Porta a direita')
        print('2: Porta a frente')
        print('3: Porta a esquerda')
        porta7 = int(input('> '))
                
        if tranca7 == True and porta7 == 1 and chave > 0:
                print('Você usa uma chave e destranca a porta a direita')
                tranca7 = False
                tranca7W = False
        elif porta7 == 1 and chave == 0:
                print('Chaves insuficientes')

        else:
            tranca7W = False

    if porta7 == 1:
        #sala 8
        if prim8:
            print('Você encontra a ruína de uma forja nessa sala.')
            print('dentro da forja você encontra uma espada grande(5 de durabilidade).')
            print('Você pega a espada.')
            espada = 5
            prim8 = False

         #estrutura de repetição que repete a sala 8 caso o jogador não tenha uma chave e tente abrir a tranca
        tranca8W = True
        while tranca8W:
            print('Nessa sala há duas portas.')
            if tranca8 == True:
                print('1: porta demoníaca que está trancada(1 chave)')
            else:
                print('1: uma porta demoníaca')
            print('2: Porta de ferro')
            porta8 = int(input('> '))

            if porta8 == 1 and tranca8 == False:
                tranca8W = False

            elif porta8 == 1 and chave > 0:
                print('Você usa uma chave e destranca a porta a demoníaca')
                tranca8 = False
                tranca8W = False
            
            elif porta8 == 1 and chave == 0:
                print('Chaves insuficientes')

            else:
                tranca8W = False
                porta7 = 2 #Leva o jogador para a sala 9
            
        if porta8 == 1:
            #Sala 11(demônio e saída)
            if dem11:
                print('Você encontra um poderoso demônio nessa sala')
                print('Será necessário 5 de durabilidade da espada para derrotar')
                print(f'Sua espada tem {espada} de durabilidade')
                print('1: Lutar')
                input('> ')
                if espada > 4:
                    print('Você derrota o demônio com sucesso')
                    espada -= 1
                    dem11 = False
                else:
                    espada -= espada
                    print('Sua espada quebra na luta e você fica indefeso')
                    if pocao > 0:
                        print('Você bebe uma poção de retorno e sobrevive, retornando à primeira sala')
                        pocao -= 1
                    else:
                        print('Você morreu')
                        vida = False
                
                print('Essa sala tem duas saídas.')
                print('1: porta de madeira')
                print('2: Você ve uma luz nessa direção, a saída possívelmente?')
                porta11 = int(input('> '))

                if porta11 == 1:
                    porta7 = 2
                else:
                    print('Você entra no túnel com a luz, caminhando nessa direção você encontra a saída.')
                    print('1: Em frente(terminar o jogo).')
                    input('> ')
                    print('Parabéns, você escapou da masmorra.')
                    break #Encerra o jogo


    if porta7 == 2:
        #sala 9
        if prim9:
            print('Você encontra uma mesa com uma poção de retorno em cima')
            print('Você pega a poção')
            pocao += 1
            prim9 = False
        print('Nessa sala você vê duas portas')
        print('1: Direita')
        print('2: Esquerda')
        porta9 = int(input('> '))

        if porta9 == 1:
            #Armadilha
            print('Você cai em uma armadilha')
            if pocao > 0:
                print('Você bebe uma poção de retorno e sobrevive, retornando à sala da fogueira.')
                pocao -= 1
            else:
                print('Você morreu.')
                vida = False
        
        else:
            #Sala 12
            print('Você vê duas portas nessa sala')
            print('1: Uma porta de ferro')
            print('2: Uma porta aberta, você pode ver uma luz na sala a diante')
            porta12 = int(input('> '))
            if porta12 == 1:
            #Sala 13
                if cac13:
                    print('Você encontra um caçador nessa sala')
                    print('Será necessário 2 de durabilidade da espada para derrotar')
                    print(f'Sua espada tem {espada} de durabilidade')
                    print('1: Lutar')
                    input('> ')
                    if espada > 1:
                        print('Você derrota o caçador com sucesso')
                        espada -= 3
                        cac13= False
                    else:
                        print('Sua espada quebra na luta e você fica indefeso')
                        espada -= espada
                        if pocao > 0:
                            print('Você bebe uma poção de retorno e sobrevive, retornando à primeira sala')
                            pocao -= 1
                        else:
                            print('Você morreu')
                            vida = False

                print('Você pode ver duas portas nessa sala')
                print('1: Porta de ferro ensanguentada')
                print('2: porta de ferro com espinhos')
                porta13 = int(input('> '))
                if porta13 == 1:
                    #Armadilha 1
                    print('Você cai em uma armadilha')
                    if pocao > 0:
                        print('Você bebe uma poção de retorno e sobrevive, retornando à sala da fogueira.')
                        pocao -= 1
                    else:
                        print('Você morreu.')
                        vida = False
                else:
                    #Armadilha 2
                    print('Você cai em uma armadilha')
                    if pocao > 0:
                        print('Você bebe uma poção de retorno e sobrevive, retornando à sala da fogueira.')
                        pocao -= 1
                    else:
                        print('Você morreu.')
                        vida = False
        
            else:
                #Levar para sala 14
                porta10 = 2
            


    else:
        #sala 10
        if porta10 == 0:
            print('Há duas portas nessa sala')
            print('1: Esquerda')
            print('2: Em frente')
            porta10 = input('> ')


        if porta10 == 1:
            #Armadilha
            print('Você cai em uma armadilha')
            if pocao > 0:
                print('Você bebe uma poção de retorno e sobrevive, retornando à sala da fogueira.')
                pocao -= 1
            else:
                print('Você morreu.')
                vida = False
        else:
            #Sala 14
            print('Há apenas uma porta nessa sala, quanto mais você se aproxima, mais forte a luz emanando dela vai ficando')
            print('1: Em frente(terminar o jogo)')
            int(input('> '))
            print('Parabéns, você escapou da masmorra.')
            break #Encerra o jogo


