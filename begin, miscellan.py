print("Alo mundo!")
for x in range(0,5):
    print('x vale', x)
    
print('este código realiza soma de dois números')

#é necessário converter o input(entrada dos dados) em número, int ou float
#isso pode ser feito na hora de pedir:
A=int(input('insira o comprimento A:'))
B=int(input('insira o comprimento B:'))
soma1 = A+B
print('O 1o resultado é',soma1)

#ou pode ser convertido depois!
C=input('insira primeiro valor:',)
D=input('insira o segundo valor:')
C=int(C)
D=int(D)
#inicialmente C e C são strings, aqui eu Redefino C e D como números inteiros
soma2 = C+D
print('olha como a segunda soma funciona tb:',soma2)