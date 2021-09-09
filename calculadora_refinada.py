import sys   # lembre de importar sys
import math                 # CALCULA VARIAS FUNÇÕES MATEMÁTICAS, COM ENTRADAS PADRONIZADAS

for linha in sys.stdin:   # linha é uma variável que (por alguma razão) em sys.stdin pega cada _entrada_ por ""linha""" ((stdin é a "Porta"))
    conta = linha.split(' ') # conta é uma lista de cada elemento de linha dividido por ' '
    funçao = conta[0]
    x = float(conta[1])
    if len(conta) == 3:         # considerando diferentes funções da calculadora, algumas usam dois números: 'SUM 3 4'
        y = float(conta[2])
    if funçao == 'SUM':
            print('{:.2f}'.format(x+y))
    elif funçao == 'DIF':
        print('{:.2f}'.format(x-y))
    elif funçao == 'MULT':
        print('{:.2f}'.format(x*y))
    elif funçao == 'DIV':
        if y == 0:                  # excluindo divisão por zero como conta válida
            print('Operacao Invalida')
        else: print('{:.2f}'.format(x/y))
    elif funçao == 'POT':
            print('{:.2f}'.format(x**y))
    elif funçao == 'RAIZ':
            print('{:.2f}'.format(math.sqrt(x)))
    elif funçao == 'LOG10':
            print('{:.2f}'.format(math.log10(x)))          # biblioteca math
    else: print('Operacao Invalida')        # se a entrada n estiver no formato certo, não é válido



'''import math
pedido = [] # criando uma lista vazia em 'pedido'
operaçao = input()
while operaçao != " ": # enquanto na entrada vier algo diferente de nada, faça:
    pedido.append(operaçao) # adiciona na lista a entrada recebida
    operaçao = input() # REDEFINE 'OPERAÇAO' PARA TER UM POSSÍVEL NOVO INPUT; verifica se há nova entrada assim que recomeça o while

    for i in pedido: # >>>>   Vai Repetir o Processo para CADA UM Dos Índices 'i' que Houver na Lista 'Pedido'
        conta = i # dividir a string do índice em diferentes pedaços, formando uma lista 'conta'
        funçao = conta[0]
        x = float(conta[1])
        if len(conta) == 3:
            y = float(conta[2])
        
        if funçao == 'SUM':
            print('{:.2f}'.format(x+y))
        elif funçao == 'DIF':
            print('{:.2f}'.format(x-y))
        elif funçao == 'MULT':
            print('{:.2f}'.format(x*y))
        elif funçao == 'DIV':
            if y == 0:
                print('Operacao Invalida')
            else: print('{:.2f}'.format(x/y))
        elif funçao == 'POT':
            print('{:.2f}'.format(x**y))
        elif funçao == 'RAIZ':
            print('{:.2f}'.format(math.sqrt(x)))
        elif funçao == 'LOG10':
            print('{:.2f}'.format(math.log10(x)))
        else: print('Operacao Invalida')'''