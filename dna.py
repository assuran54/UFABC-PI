extensao = input()                  # DEVOLVE A SEQUÊNCIA DE NUCLEOTÍDEOS COMPLEMENTAR À SEQUÊNCIA FORNECIDA, COMO TB SUA EXTENSÃO EM NUCLEOTÍDEOS
extensao = extensao.split()                             # (entrada recebe tb a extensão em linhas do dna fornecido)
extensao = int(extensao[1]) # de '> 5' pega só o 5
                                                # if you know that there are no spaces in your data, you can use split() (with no arguments)
                                                # This splits on white spaces and is efficient. It also strips whitespace from both ends.
fita1 = []
nucleotideos = 0

def desmonte (lin):  # desmontar uma linha duma string só
    for n in lin:
        fita1.append(n)        # ainda me confundo com o uso de funções [VIDE 'EDU_MATRIZ']

def complemento (n): # será q n tem jeito melhor de fazer não? Como ??
    if n == 'a':
        n = 't'
    elif n == 't':
        n = 'a'
    elif n == 'c':
        n = 'g'
    elif n == 'g':
        n = 'c'
    return n

count = 0
'''try:'''
while count < extensao:  # nesse caso contar até extensão dada não seria necessário 
    linha = input()      # pq 'try except' com 'while True' já faz até n dar mais
    if linha == '':
        break
    desmonte(linha)
    count += 1
'''except EOFError: pass             Após completo, removi try except pq acho q na real não precisa, pois o count já barra o EOF.'''   

fita2 = []
for base in fita1:
    nucleotideos += 1
    par = complemento(base)  # bota a sequencia complementar da fita dada, conforme pedido
    fita2.append(par)

count = 0
print('>', nucleotideos)
for base in fita2:       # deve fazer com que haja apenas 20 nucleotídeos no máximo por linha
    count += 1
    print(base, end = ('' if count < 20 else '\n'))  # sem espaço ('') caso contagem n chegou a 20, else nova linha
    if count == 20:
        count = 0
