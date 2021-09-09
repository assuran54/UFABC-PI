extensao = int(input())
velha = []                      # DEVOLVE O VITORIOSO DE UM JOGO DA VELHA A PARTIR DO TABULEIRO, PREENCHIDO (e uma dada extensão)
cont = 0                            # pode haver empates, resultados impossíveis de determinar e erro na sequência de jogadas
while cont < extensao:
    linha = input()
    linha = list(linha)     # Meio ótimo de separar caracteres de uma string, formando uma lista!!
    velha.append(linha)                        # esse trecho em geral: jeito prático de montar matriz (de str, inputs sem supérfluos)
    cont += 1

def horizontais(velha):     # registra numa lista o placar de cada possível vitória na horizontal
    res = []
    for lin in velha:     # Para cada linha, cria-se um contador do placar,
        horiz = 0
        for c in lin:
            if c == 'X':        # o placar sobe um para cada X encontrado, e desce um para cada O encontrado
                horiz += 1
            else: horiz -= 1        # linhas com placares cujo módulo do valor é igual à extensão são linhas onde há hegemonia
        res.append(horiz)       # cada linha tem seu placar registrado numa lista

    return res

def verticais(velha):     # Registra numa lista o placar de cada possível vitória na vertical
    res = []
    for col in velha[0]:  # usando a primeira linha como referência para o nº de colunas, gera-se um placar para cada uma
        vert = 0
        for n in range(extensao):
            #print(velha[0].index(col))
            #if velha[n][velha[0].index(col)] == 'X':                    
            # velha[l][col] <- NÃO pode (type error List cannot pose as index/integer (sobre o l))
            if velha[n][len(res)] == 'X':       # Percorre a matriz, olhando o placar daquela coluna em cada das 'n' linhas q há.
                vert += 1                       # A coluna a analisar da vez vai depender de quantas colunas já foram
            else: vert -= 1                     # adicionadas na lista de placares contados (res), então serve de contador:
        res.append(vert)                        # pra cada placar de coluna feito, o comprimento da lista aumenta em um.

    return res
        
def diagonais(velha):       # Registra numa lista o placar das duas possíveis vitórias na diagonal
    res = []
    diag1 = 0
    diag2 = 0
    for n in range(extensao):         # diagonal 1 vai do topo esquerdo ao fundo direito
        if velha[n][n] == 'X':        # as coordenadas de linha e coluna crescem juntas conforme avança na diagonal
            diag1 += 1
        else: diag1 -= 1

        if velha[extensao-1-n][n] == 'X':  # velha[extensao-lin][lin]   < erro
            diag2 += 1                  # diagonal do fundo esquerdo ao topo direito
        else: diag2 -= 1                # a coordenada de linha diminui enquanto a coluna avança
    res.append(diag1)
    res.append(diag2)

    return res

vitoria_X = False
vitoria_O = False
for i in horizontais(velha):        # para cada linha da velha verifica se
    if i == extensao:               # há linha com apenas X
        vitoria_X = True
    elif i == -extensao:            # ou linha com apenas O
        vitoria_O = True
for i in verticais(velha):          # pra cada coluna da velha verifica se
    if i == extensao:               # há coluna composta somente de X, ou coluna somente de O
        vitoria_X = True
    elif i == -extensao:
        vitoria_O = True
for i in diagonais(velha):          # para cada uma das duas diagonais, verifica o caso de haver apenas X, ou haver apenas O
    if i == extensao:
        vitoria_X = True
    elif i == -extensao:
        vitoria_O = True
nX = 0
nO = 0
for lin in velha:           
    for col in lin:         # conta o número de X e Os no tabuleiro
        if col == 'X':
            nX += 1
        else: nO += 1

if abs(nX - nO) > 1:            # se o tabuleiro tem uma diferença de X e Os maior que um, a sequência de jogadas n foi cumprida
    print('UM DOS JOGADORES JOGOU MAIS DO QUE DEVERIA')     # mas, se foi cumprida:
else:
    if vitoria_X == True and vitoria_O == True:   # se ambos jogadores tiverem lugares de vitória, n dá pra saber quem ganhou primeiro
        v = 'INDETERMINADO'
    elif vitoria_X == False and vitoria_O == False:   # é empate quando ninguém consegue uma sequência vitoriosa
        v = 'EMPATE'
    elif vitoria_X == True and vitoria_O == False:
        v = 'X'
    elif vitoria_X == False and vitoria_O == True:
        v = 'O'
    print('Vencedor:', v)