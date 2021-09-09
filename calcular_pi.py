import sys

                            # DEVOLVE APROXIMAÇÃO DE PI, ITERANDO N VEZES OS TERMOS DA FÓRMULA DE LEIBNIZ; QTD FORNECIDA DE Ns: LIVRE
for n in sys.stdin: 
    n = int(n)

    ite = 1
    while ite <= n:
        soma = 0
        
        for k in range(n):
            soma = soma + ((-1)**k)/(2*k + 1)
            pi = 4*soma
            ite = ite + 1
        print('pi(',n,') =','{:.4f}'.format(pi))
        

    


'''n = int(n)
    denom = 1
    sinal = 1                        # Primeira tentativa
    ite = 1
    while ite <= n:
        for k in range(0,n):
            pi = 4*(1+k*(1/denom))
        denom = denom + (2*-1**sinal)
        print(denom)
        sinal = sinal + 1
        ite = ite + 1    
    print('{:.4f}'.format(pi))'''

'''    n = int(input())          # Segunda tentativa, deu erro na formula de pi em si, fui atrás dela na net
denom = 1                               # n posso ficar tentando inventar matemática
absol = 1
sinal = 1

for k in range(0,n):
    pi = 4*(1+k*(1/denom))
    print('{:.4f}'.format(pi))
    sinal = sinal*-1
    absol = absol + 2
    denom = absol*sinal'''