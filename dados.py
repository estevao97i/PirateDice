import random
import time 

def calcularProbabilidade(listaJogador, listaRobo, numeroEscolhido, quantidade):
    somatorio = 1
    ocorrenciasNumeroListaRobo =  quantidade - listaRobo.count(numeroEscolhido) 

    if (ocorrenciasNumeroListaRobo <= 0):
        return False
    for _ in range(ocorrenciasNumeroListaRobo):
        somatorio *= (1 / len(listaJogador))
    return somatorio * 100


def girarDados(numDadosMao, numDadosRobo):

    dadosMao = []
    dadosRobo = []

    if (numDadosMao == 0):
        print('Você perdeu o jogo :(')
        return
    elif (numDadosRobo == 0):
        print('Parabéns, você ganhou o jogo <3')
        return 

    for _ in range(numDadosMao):
        dadoMao = random.randint(1,6)
        dadosMao.append(dadoMao)

    for _ in range(numDadosRobo):
        dadoRobo = random.randint(1,6)
        dadosRobo.append(dadoRobo)

    print('gerando dados...')
    time.sleep(3)

    print('---------------------------------------------------------------')
    print()
    # print(f' {dadoImg(dadosMao[0])} {dadoImg(dadosMao[1])} {dadoImg(dadosMao[2])} {dadoImg(dadosMao[3])}')
    print('Seus dados são:', dadosMao)
    print()

    print('---------------------------------------------------------------')
    print(f'Sabendo que seu oponente lançou {numDadosRobo} dados aleatórios, faça a sua aposta...')
    print('---------------------------------------------------------------')
    time.sleep(1)

    apostar(dadosMao, dadosRobo)

    # TO DO
    # Arrumar essa logica para o computador também ganhar... (colocar um if e receber quem está afirmando)

def ganhadorPerdedor(numAposta, ocorrencias, dadosMao, dadosRobo, quemEscolheu):
    if (quemEscolheu == 'robo'):
        if (dadosMao.count(numAposta) + dadosRobo.count(numAposta) >= ocorrencias):
                    print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=')
                    print('VOCÊ ACERTOU!')
                    print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=')
                    print("dados do seu oponente:", dadosRobo)
                    print()
                    print('Seu oponente perdeu um dado!')
                    print()
                    return True
        print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=')
        print('VOCÊ PERDEU :(')   
        print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=')
        print("dados do seu oponente:", dadosRobo)
        print()
        print('Você perdeu um dado!')
        print()
        return False   
    
    elif (quemEscolheu == 'jogador'):
        if (dadosMao.count(numAposta) + dadosRobo.count(numAposta) >= ocorrencias):        
            print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=')
            print('VOCÊ PERDEU :(')   
            print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=')
            print("dados do seu oponente:", dadosRobo)
            print()
            print('Você perdeu um dado!')
            print()
            return False 
        print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=')
        print('VOCÊ ACERTOU!')
        print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=')
        print("dados do seu oponente:", dadosRobo)
        print()
        print('Seu oponente perdeu um dado!')
        print()
        return True 

def resultadoAposta(numAposta, ocorrencias, dadosMao, dadosRobo, quemEscolheu):
    if(quemEscolheu == 'robo'):
        print(f"Seu adversário disse que não tem {ocorrencias}' {numAposta} no jogo!")
        print('Seus dados são:', dadosMao)
        return ganhadorPerdedor(numAposta, ocorrencias, dadosMao, dadosRobo, quemEscolheu='robo')
    elif (quemEscolheu == 'jogador'):
         print(f"Você afirma que não tem {ocorrencias}' {numAposta} no jogo!")
         return ganhadorPerdedor(numAposta, ocorrencias, dadosMao, dadosRobo, quemEscolheu='jogador')

def apostar(dadosMao, dadosRobo):

    print('Escolha uma número para apostar: |[1]| |[2]| |[3]| |[4]| |[5]| |[6]| ')
    numAposta = int(input())

    print(f'Quantos {numAposta} tem no jogo?')
    ocorrencias = int(input())

    resultado = None

    resultadoProbabilidade = calcularProbabilidade(listaJogador=dadosMao, listaRobo=dadosRobo, numeroEscolhido=numAposta, quantidade=ocorrencias)

    if (resultadoProbabilidade < 8 or resultadoProbabilidade == True):
        resultado = resultadoAposta(numAposta, ocorrencias, dadosMao, dadosRobo, quemEscolheu='robo')

    if (resultado == False):
        return girarDados(numDadosMao=len(dadosMao) - 1, numDadosRobo=len(dadosRobo))
    elif (resultado == True):
        return girarDados(numDadosMao=len(dadosMao), numDadosRobo=len(dadosRobo) - 1)

    print('Seu adversário acha que está correta a vossa aposta...')
    time.sleep(1.5)

    resultadoIncidencias = 0
    dadosChuteRobo = None

    for dado in dadosRobo:
        if (dadosRobo.count(dado) > resultadoIncidencias):
            resultadoIncidencias = dadosRobo.count(dado)
            dadosChuteRobo = dado

    resultadoIncidencias += 1

    print(f"Aposta do seu adversário é: {resultadoIncidencias} -> {dadosChuteRobo}' no jogo")

    print('==========================================================')
    print('==========================================================')
    print('            SEU ADVERSÁRIO ESTÁ MENTINDO?                 ')
    print('==========================================================')
    print('==========================================================')
    time.sleep(1.5)

    print("Seus dados:", dadosMao)
    print('para contestar seu adversário escreva "mentiroso" ou "m", para aumentar aposta digite "aumentar" ou "a" ')
    escolha = input()

    if (escolha == 'mentiroso' or escolha == 'm'):

        resultado = resultadoAposta(dadosChuteRobo, resultadoIncidencias, dadosMao, dadosRobo, quemEscolheu='jogador')

        if (resultado == False):
            return girarDados(numDadosMao=len(dadosMao) - 1, numDadosRobo=len(dadosRobo))
        elif (resultado == True):
            return girarDados(numDadosMao=len(dadosMao), numDadosRobo=len(dadosRobo) - 1)

    elif (escolha == 'aumentar' or escolha == 'a'):
        apostar(dadosMao=dadosMao, dadosRobo=dadosRobo)    

def dadoImg(numeroDado):
    if (numeroDado == 1):
        print('-------------')
        print('|           |')
        print('|           |')
        print('|    000    |')
        print('|           |')
        print('|           |')
        print('-------------')

    if (numeroDado == 2):
        print('-------------')
        print('|       000 |')
        print('|           |')
        print('|           |')
        print('|           |')
        print('| 000       |')
        print('-------------')

    if (numeroDado == 3):
        print('-------------')
        print('|       000 |')
        print('|           |')
        print('|    000    |')
        print('|           |')
        print('| 000       |')
        print('-------------')

    if (numeroDado == 4):
        print('-------------')
        print('| 000   000 |')
        print('|           |')
        print('|           |')
        print('|           |')
        print('| 000   000 |')
        print('-------------')

    if (numeroDado == 5):
        print('-------------')
        print('| 000   000 |')
        print('|           |')
        print('|    000    |')
        print('|           |')
        print('| 000   000 |')
        print('-------------')

    if (numeroDado == 6):
        print('-------------')
        print('| 000   000 |')
        print('|           |')
        print('| 000   000 |')
        print('|           |')
        print('| 000   000 |')
        print('-------------')

    return ''

print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
print('| BEM VINDO AO PIRATE DICE |')
print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
print('aperte ENTER parar girar os dados!')
enter = input()

numDadosMao = 2
numDadosRobo = 2

girarDados(numDadosMao=numDadosMao, numDadosRobo=numDadosRobo)



    






