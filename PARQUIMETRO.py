chegada = input()
chegada_str = chegada.split(':')            # CALCULA PREÇO DA ESTADIA NUM ESTACIONAMENTO DADOS HORÁRIOS DE ENTRADA E SAÍDA
saida = input()                             # 15 min tolerância, 1ª hora: 5$, 2ª a 4ª hora: 3$ cada, 5ª hora e adiante: 2$ cada
saida_str = saida.split(':')                # (considera-se hora cheia: 90 min cobra taxa de 2h)

#ATENÇAO
#VC PODE REDEFINIR ENTRADA EM CIMA DE ENTRADA.SPLIT! 

ChegHor = int(chegada_str[0])
ChegMin = int(chegada_str[1])
SaidHor = int(saida_str[0])
SaidMin = int(saida_str[1])

horas = SaidHor - ChegHor           # final menos inicial
minutos = SaidMin - ChegMin
# contar cada hora conforme categoria da hora: 7h -> 1h(5$) + 3*3/h(9$) + 3*2/h(6$) = 20$

tolerancia = 0
if horas == 0 and minutos <= 15:
    preço = tolerancia
elif minutos > 0:           # tem q ser elif pq 15 é <= 15 E é > 0
    horas = horas + 1       # hora quebrada sempre arredonda pra cima

if horas == 1 and minutos <= -45:       # -45 a -59 pra contabilizar casos 00:50 > 01:05 (por ex)
    preço = tolerancia
elif horas >= 1:
    preço = 5

if horas >= 2 and horas < 5:    # vai somar em cima do preço da 1ª hora
    preço = preço + (horas-1)*3
elif horas >= 5:          # tem q ser elif pq senão 5ª hora tb vai multiplicar por 3
    preço = preço + 9 + (horas-4)*2
# meio sujo colocar "+9", mas n sei um modo limpo; +9 contabiliza as horas de 2 a 4, ignoradas no elif       < (retrospectiva: como tirar o 9?)

# print('Permanência: ',horas,'horas e',minutos,'minutos')
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