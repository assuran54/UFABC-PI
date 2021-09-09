dimensao = input()
dimensao = dimensao.split()             # DIZ QUANTOS NÚMEROS ÚNICOS SE REPETEM NA MATRIZ FORNECIDA; não se conta duas vezes o mesmo número
linhas = int(dimensao[0])                   # (dimensões da matriz são fornecidas antes)
colunas = int(dimensao[1])    
        # note que não usei 'colunas' no código, pq bastou usar 'for k in linha'
cont = 0
M = []
while cont < linhas:
    lin = input()
    lin = lin.split()
    lin = [int(i) for i in lin]   # meio esperto de converter cada i da lista em int. (for na mesma linha! (que nem if))   !!!!
    M.append(lin)         # é adicionada dentro do vetor(lista) M cada linha da Matriz que for fornecida
    cont += 1

def acha_replica (k):       # Compara cada elemento da matriz com um valor k fornecido, faz contagem das repetições, devolve bool
    gemeos = False
    n = 0
    for l in M:
        for i in l:
            if i == k:      # olha cada elemento de cada linha e compara com o valor k fornecido
                n += 1
    if n >= 2:              # é 2 pq conta o original tb
        gemeos = True
    return gemeos

vistos = []
N = 0
for lin in M:
    for k in lin:
        Go = True
        for j in vistos:
            if k == j:          # se for encontrado o valor de k na lista dos já vistos, não segue
                Go = False
        if Go:
            if acha_replica(k):     # sabido que k é inédito (n repita gemeos já identificados), verifico que se ele tem gemeos
                N += 1      # números de gemeos
        vistos.append(k)    # adiciona valor de k à lista de já analisados

print(N)


'''for l in range(linhas):
    for c in range(colunas):
        if M[l][c] == i:
            gemeos += 1
            break'''
