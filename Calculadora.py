pedido = input()
operaçao = pedido.split(' ')
# .split() no parenteses está o símbolo que representa o local de divisão, split

funçao = operaçao[0]
x = float(operaçao[1])
#LEMBRE QUE PRA COMPARAÇÃO É O ==
if len(operaçao) == 3:
    y = float(operaçao[2])


#Exatamente dois decimais -> '{:.2f}'.format()

# Atenção! 

# Atribuição: '='; Comparação: '=='

import math
if funçao =='SUM':
    print('{:.2f}'.format(x+y))
elif funçao == 'DIF':
    print('{:.2f}'.format(x-y))
elif funçao == 'MULT':
    print('{:.2f}'.format(x*y))
elif funçao == 'DIV':
    print('{:.2f}'.format(x/y))
elif funçao == 'POT':
    print('{:.2f}'.format(x**y))
elif funçao == 'RAIZ':
    print('{:.2f}'.format(math.sqrt(x)))
#math.sqrt    tem q botar "math."!
elif funçao == 'LOG10':
    print('{:.2f}'.format(math.log10(x)))