dimensao = input()
dimensao = dimensao.split()
N = int(dimensao[0])            # VERIFICA SE A MATRIZ FORNECIDA É UMA MATRIZ ESCADA; (recebe antes o comprimento e altura da matriz)
M = int(dimensao[1])                 # 1: se uma linha da matriz é de zeros, todas linhas abaixo tem apenas zeros
                                     # 2: sendo X o elemento diferente de 0 mais à esquerda, todos elementos abaixo e à esquerda de X são zeros
matriz = []
cont = 0
while cont < N:
    linha = input()
    linha = linha.split()
    linha = [int(i) for i in linha]     # converte todo i da linha em int, de uma vez
    matriz.append(linha)
    cont += 1

def asa_esquerda(linha,coluna):     # assume estar certo, para procurar erros (ie um x != 0) em cada casa que estiver: 
    asa = True                      # à esquerda do lead E abaixo do lead. Devolve o res da verificação
    for lin in matriz[linha + 1:]:
        for x in lin[:coluna + 1]:  # [linha+1:] significa: inicia na linha abaixo da lead, termina no fim de 'matriz'
            if x != 0:              # [:coluna+1] significa: inicia da 1ª coluna, termina na coluna de lead
                asa = False
    return asa

def clean (lin0):                   # Verifica as casas de linhas que estiverem abaixo da linha-referência que não sejam zeros
    clean = True                    # para retornar essa verificação
    for linha in matriz[lin0:]:
        for x in linha:
            if x != 0:
                clean = False
    return clean

escada = True
for linha in matriz:
    zeros = 0
    lead = 0
    for x in linha:
        if x != 0:
            if lead == 0:
                lead = x
                lin_lead = matriz.index(linha)      # método pra extrair a localização do elemento numa lista
                col_lead = linha.index(lead)
        else: zeros += 1
    if zeros == M:
        if clean(matriz.index(linha)) == False:      # não pode ser 'linha' direto pq aqui ela é uma lista cheia de x
            escada = False
            break
    elif asa_esquerda(lin_lead,col_lead) == False:      # do processo: tive q deixar elif pq se n falhava em matrizes de zeros
        escada = False
        break

if escada:
    print('S')
else: print('N')

                        # 3 Formas de se printar uma lista/string revertida, do fim pro começo
''' # for i in list[::-1]:      print(i)
    # for i in reversed(list):      print(i)           
    # for i in range(len(list) -1, -1, -1):     print(list[i])'''