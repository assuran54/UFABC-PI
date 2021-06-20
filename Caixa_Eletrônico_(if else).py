#NÃO PRECISA DE IF

saque = float(input())

#se valor for maior q C, dividir por C e pegar o inteiro em cédulas. Subtrair quantia e seguir os Cs, até zerar
#deve ter jeitos mais eficientes, queria saber como

#não precisa de int do saque//x
while True:
 if(saque>=100):
  c100=saque//100
  saque=saque-c100*100
 else: c100=0
 if(saque>=50):
  c50=saque//50
  #saque=saque%50         podia usar o módulo pra pegar o restante
  saque=saque-c50*50
 else: c50=0
 if(saque>=20):
  c20=saque//20
  saque=saque-c20*20
 else: c20=0
 if(saque>=10):
  c10=saque//10
  saque=saque-c10*10
 else: c10=0
 if(saque>=5):
  c5=saque//5
  saque=saque-c5*5
 else: c5=0
 if(saque>=2):
  c2=saque//2
  saque=saque-c2*2
 else: c2=0
 if(saque>=1):
  c1=saque//1
  saque=saque-c1*1
 else: c1=0
 break

print(saque)

print('Cédulas de R$ 100.00:',c100)
print('Cédulas de R$ 50.00:',c50)
print('Cédulas de R$ 20.00:',c20)
print('Cédulas de R$ 10.00:',c10)
print('Cédulas de R$ 5.00:',c5)
print('Cédulas de R$ 2.00:',c2)
print('Cédulas de R$ 1.00:',c1)