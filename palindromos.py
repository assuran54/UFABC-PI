extensao = int(input())
                                # VERIFICA SE CADA FRASE FORNECIDA É UM PALÍNDROMO; desconsidera tudo q n for letrana análise
entradas = []
contagem = 0
while contagem < extensao:      # lê e armazena entradas até alcançar a extensao de entradas
    frase = input()
    entradas.append(frase)
    contagem += 1

def palindromo(l):              # compara a primeira e última letra, e vai migrando pro centro. Se não for igual, parou
    m = 0                       # note que, se tiver uma letra mediana, ela não é analisada
    pal = 'SIM'
    while m < (len(l)//2):                    # m faz comparação mover pro centro, ao chegar lá, deve-se parar de comparar
        if l[0 + m] != l[len(l) - 1 - m]:     # se prineira letra do palindromo for diferente da última
            pal = 'NAO'                       # a cada iteração a comparação migra uma casa pro centro, m
            break
        m += 1
    return pal

for frase in entradas:
    sequencia = []
    for symb in frase:           # if isalpha serve pra só analisar letras na função palindromo
        if symb.isalpha():       #(ord(symb) >= 97 and ord(symb) <= 122) or (ord(symb) >= 65 and ord(symb) <= 90):        < alternativa
            symb = symb.lower()     # deixa tudo no minúsculo pq python vê diferença entre letras grandes e pequenas, não identificaria igualdade
            sequencia.append(symb)
    print(palindromo(sequencia))