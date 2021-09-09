conjunto = []
                            # GERA MÉDIA, VARIÂNCIA E DESVIO PADRÃO DO CONJUNTO DE NÚMEROS FORNECIDO
try:
    while True:        # <<<< Formato interessante/importante!
        a = input()
        if a == '':
            break
        conjunto.append(float(a))
except EOFError: pass               # try except aqui serve pra q o erro end of file não aconteça 
                                    # quando o programa não achar um input pra receber, seguindo adiante:  pass
quantia = len(conjunto)
                    # quantia de termos no conjunto agregado
med = 0
for x in conjunto:  # conjunto é a lista dos nums
    med += x            #   <<<<<< EQUIVALE A: med = med + x
Media = med/quantia
print('media =','{:.2f}'.format(Media))          # média=(x1+x2+x3+x4)/n

var = 0
for x in conjunto:
    tmp = (x - Media)**2
    var += tmp
    if quantia == 1:    # não divida por zero (fórmula de variancia faz dividir por quantia - 1)
        Variancia = 0
    else: Variancia = var/(quantia - 1)
print('variancia =','{:.2f}'.format(Variancia))      # variancia=((x1-média)**2+(x2-média)**2+(x3-média)**2+(x4-média)**2)/n-1

import math
Desvio = math.sqrt(Variancia)
print('desvio =','{:.2f}'.format(Desvio))