import sys       # ACHA NÚMEROS PRIMOS NO INTERVALO ENTRE UM PAR DE NÚMEROS FORNECIDOS; Nº DE PARES FORNECIDOS: LIVRE


for linha in sys.stdin:
    intervalo = linha.split()       # para cada linha de entrada q se receber, determina-se os limites de tal intervalo dado
    x1 = int(intervalo[0])          # e parte-se do limite menor com a análise de primidade
    x2 = int(intervalo[1])
    foco = x1
    primos = [] # a cada iteração(linha) ele vai zerar a lista de primos 

    while foco <= x2: # repete o processo para testar, ser primo ou não, todo número que se encontra dentro do intervalo dado naquela linha
        primo = True
        
        for divisor in range(2,x2+1): # olha divisores de 2 ao intervalo máximo ((não existe divisor inteiro maior que o número em si))
            if (foco % divisor == 0 and foco != divisor) or foco == 1: # jeito bizarro de excluir 1 do output de primos
                primo = False  # note na condiçao que devo desconsiderar divisão por si mesmo, pq isso n diferencia não primos de primos
                break # só pra n verificar todos os divisores
        
        if primo == True: # podia ser só "if primo:" q ia funcionar. ambos valores booleanos
                primos.append(foco) # cada primo que não foi falseado é adicionado na lista 'primos'
                
        foco = foco + 1
    
    print(*primos) # printing the list using * operator separated by space "print(*list)"
                    # gera: <1 2 3 4 5>

                    # print(*list, sep = ", ") assim cada valor é separado por vírgula
                    # (*list, sep = "\n") vai separar valores por linha
