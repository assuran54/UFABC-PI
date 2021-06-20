chegada = input()
chegada_str = chegada.split(':')
saida = input()
saida_str = saida.split(':')

#ATENÇAO
#VC PODE REDEFINIR ENTRADA EM CIMA DE ENTRADA.SPLIT! 

ChegHor = int(chegada_str[0])
ChegMin = int(chegada_str[1])
SaidHor = int(saida_str[0])
SaidMin = int(saida_str[1])

horas = SaidHor - ChegHor
minutos = SaidMin - ChegMin
#contar cada hora conforme categoria da hora: 7h -> 1h(5$) + 3*3/h(9$) + 3*2/h(6$) = 20$

tolerancia = 0
if horas == 0 and minutos <= 15:
    preço = tolerancia
#tem q ser elif pq 15 é <= 15 E é > 0
elif minutos > 0:
    horas = horas + 1
#hora quebrada sempre arredonda pra cima
if horas == 1 and minutos <= -45:
    preço = tolerancia
# -45 a -59 pra contabilizar casos 00:50 > 01:05 (ex)

elif horas >= 1:
    preço = 5
if horas >= 2 and horas < 5:
    preço = preço + (horas-1)*3
#tem q ser elif pq senão 5ª hora tb vai multiplicar por 3
elif horas >= 5:
    preço = preço + 9 + (horas-4)*2
#meio sujo colocar "+9", mas n sei um modo limpo

#print('Permanência: ',horas,'horas e',minutos,'minutos')
print('R$',preço,'.00')


'''import math

entrada = input()
saida = input()

entrada = entrada.split(':')
saida = saida.split(':')

minuto_entrada = float(entrada[1]) / 60
hora_entrada = float(entrada[0]) + minuto_entrada

minuto_saida = float(saida[1]) / 60
hora_saida = float(saida[0]) + minuto_saida

periodo = hora_saida - hora_entrada

if(periodo <= 0.25):
    custo = 0
    print("R$ = %.2f" %custo)
else:
    periodo = math.ceil(periodo)
   
    if(periodo < 2.00):
        custo = 5 * periodo
        print("R$ = %.2f" %custo)
    elif((periodo > 2.00) and (periodo <= 4.00)):
        custo = 5 + (3 * (periodo - 1))
        print("R$ = %.2f" %custo)
    else:
        custo = 14 + (2 * (periodo - 4))
        print("R$ = %.2f" %custo)
        '''