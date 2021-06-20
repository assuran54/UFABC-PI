lados = input()
#redefinindo em cima de lados
lados = lados.split(' ')
#não posso iniciar convertido em float "float(input()" pois o .split só funciona em string

a = float(lados[0])
b = float(lados[1])
c = float(lados[2])

if b > a:
    tmp = a
    a = b
    b = tmp
if c > a:
    tmp = a
    a = c
    c = tmp
# aqui tá feito que o maior lado seja necessariamente 'a'
if c > b:
    tmp = b
    b = c
    c = tmp

if a <= 0 or b <= 0 or c <= 0:
    print('Medidas nao formam um triangulo')
elif a >= b + c:
    print('Medidas nao formam um triangulo')
elif a == b == c:
    print('Triangulo equilatero')
#podia ter tentado usar xor para o isosceles, onde não pode ser verdade ambos, mas não consegui
#apesar disso, funciona perfeitamente !botar o equilatero antes na sequência!, e usar:  elif  'isosceles'.
elif a == b or b == c:
    print('Triangulo isosceles')
else: print('Triangulo escaleno')
