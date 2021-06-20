numeros = input('Digite três numeros: ')

num_sep = numeros.split(' ')

n1 = int(num_sep[0])
n2 = int(num_sep[1])
n3 = int(num_sep[2])

if n3 < n2:
    tmp = n2
    n2 = n3
    n3 = tmp
#assim n3 é necessariamente maior que n2
if n3 < n1:
    tmp = n3
    n3 = n1
    n1 = tmp
#n3 é o maior de todos
if n2 < n1:
    tmp = n2
    n2 = n1
    n1 = tmp
print(n3,' ',n2,' ',n1)