x1=float(input('x1:'))
x2=float(input('x2:'))
x3=float(input('x3:'))
x4=float(input('x4:'))

import math
média=(x1+x2+x3+x4)/4
variancia=((x1-média)**2+(x2-média)**2+(x3-média)**2+(x4-média)**2)/3
desvio=math.sqrt(variancia)

#string formatting to format floating point numbers to a fixed width. Decimal floating: 2 (width could be fixed at 5 like {:5.2f})
print('media =', '{:.2f}'.format(média))
print('variancia =', '{:.2f}'.format(variancia))
print('desvio =', '{:.2f}'.format(desvio))