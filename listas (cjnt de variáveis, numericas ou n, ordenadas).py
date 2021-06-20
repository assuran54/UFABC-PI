lista=[4,7,'livio',3,8]
print(lista)
[4, 7, 'livio', 3, 8]
lista.append('tito')
print(lista)
[4, 7, 'livio', 3, 8, 'tito']
lista.append(21)
print(lista)
[4, 7, 'livio', 3, 8, 'tito', 21]
lista.index('livio')
2
lista.index(21)
6
lista.count(8)
1
lista.count('robert')
0
lista.append(8)
lista.count(8)
2
print(lista)
[4, 7, 'livio', 3, 8, 'tito', 21, 8]
lista.remove(8)
print(lista)
[4, 7, 'livio', 3, 'tito', 21, 8]
lista.reverse()
print(lista)
[8, 21, 'tito', 3, 'livio', 7, 4]
lista2=[3,7,9,23,1]
print(lista2)
[3, 7, 9, 23, 1]
lista2.sort()
print(lista)
[8, 21, 'tito', 3, 'livio', 7, 4]
print(lista2)
[1, 3, 7, 9, 23]
