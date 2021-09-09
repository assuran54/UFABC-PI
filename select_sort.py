def troca (a, b):    # troca valores de posição
    return b, a                                 # RECEBE LISTA DE N NÚMEROS E ORDENA POR CRESCENTE VIA SELECTION SORT; devolve cada passo
                                                    # selection sort pega o menor elemento da parte não ordenada e bota ele na max esquerda
def menor (V):      # acha o menor valor do subvetor
    menor = V[0]
    for x in V:
        if x < menor:
            menor = x
    return menor

def posi_menor (V, i):     # localiza o menor valor do subvetor;  
    menor = V[0]
    for x in V:            # faz o msm trabalho da função 'menor', com um passo a mais, de localizar   > Como pode ser mais eficiente??
        if x < menor:
            menor = x
    p = V.index(menor)     # use index pra identificar posição(índice) do menor na lista
    return p + i     # soma i pois cada subvetor inicia uma casa à direita do anterior

def trilha(V,i):              # ATRAVESSA VETOR V TROCANDO CADA CASA PELO MENOR DO SUBVETOR RESPECTIVO
    while i < len(V)-1:                                                 # i é o elemento mais a esquerda de cada subvetor
        V[posi_menor(V[i:], i)], V[i] = troca (menor (V[i:]), V[i])     # troca o valor de i com o menor valor de seu subvetor
        i += 1                                                          # próximo subvetor desordenado começa uma casa i à direita deste
        if i < len(V)-1:     
            print(str(V)[1:-1])             # até as trocas chegarem ao fim do vetor: printa vetor, sem colchetes
    V = str(V)[1:-1]                        # após ordenar tudo printe(retorne) o vetor final ((gambiarra feia pra poder printar cada passo))
    return V        # "print(str(V).strip('[]'))"    < alternativa pra tirar os colchetes

length = int(input())

V = []
cont = 0
while cont < length:            # (padronize formato:) JÁ FORNECIDA A EXTENSÃO DE ENTRADAS, 
    elemento = int(input())     # receba e conte entradas recebidas até alcançar a extensão
    V.append(elemento)
    cont += 1
print(V)
i = 0
print(trilha(V,i))


