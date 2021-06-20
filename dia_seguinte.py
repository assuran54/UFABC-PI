data = input()
data_str = data.split('/')

dia = int(data_str[0])
mes = int(data_str[1])
ano = int(data_str[2])
#Programado desse jeito não detecta possíveis entradas incorretas, como 30/02, ou 41/14/2000

# BOTE DOIS NA CONDIÇÃO! -->> ==
if mes==1 or mes==3 or mes==5 or mes==7 or mes==8 or mes==10 or mes==12:
    ultimo = 31
elif mes==4 or mes==6 or mes==9 or mes==11:
    ultimo = 30
elif mes==2:
    ultimo = 28

if dia == ultimo:
    amanha_d = 1
else: amanha_d = dia + 1

if dia == ultimo and mes==12:
    amanha_m = 1
elif dia == ultimo:
    amanha_m = mes + 1
else: amanha_m = mes

# BOTE DOIS NA CONDIÇÃO! >> == <<
if dia == ultimo and mes == 12:
    amanha_a = ano + 1
else: amanha_a = ano

# f'{variavel:02d}' | "02": quantidade de casas | f'': formata uma string
print(f'{amanha_d:02d}','/',f'{amanha_m:02d}','/',amanha_a)