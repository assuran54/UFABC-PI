mov = int(input())
msg = input()                   # CIFRA DE CESAR, CODIFICA MENSAGEM SUBSTITUINDO LETRAS DESTA POR LETRAs X CASAS ADIANTE NO ALFABETO
                                    # tudo q n é letra não muda
'''def split(m):
    return [char for char in m]   não precisa fazer o split, pois
msg2 = split(msg)                for in já vai uma por uma da msg'''
enigma = []

for letra in msg:                 # substitui cada letra da msg pela letra mov contagens adiante
    if ord(letra) >= 97 and ord(letra) <= 122:      # só continua se o caractere está de 97 a 122 na ASCII, letras
        post = ord(letra) + mov
        if post > 122:          # se eu somar diretamente na ASCII as vezes sai do alfabeto, não quero isso, deve-se voltar ao início dele
            post = post - 26
        letra = chr(post)       # pega número da letra > move quantia nos nº da ASCII > resgata letra respectiva > add na lista/frase result
    enigma.append(letra)        # apesar de n mudar nada de chars q n são letras, eles ainda vão pra frase final (indentação)

print(msg)
print(''.join(enigma)) #quero output sem espaços entre elementos, note o ''.join, ao invés de ' '.join


    # >>>   2 métodos sobre como juntar com espaço ou sem espaço separando os elementos da lista:
'''list1=["Welcome","To","Tutorials","Point"]
string1=""
for i in list1:
   string1=string1+i
string2=""
for i in list1:
   string2=string2+i+" "
print(string1)
print(string2)

Output:
WelcomeToTutorialsPoint
Welcome To Tutorials Point

           >>>>    Using .join() method
(The list will be passed as a parameter inside the join method)

list1=["Welcome","To","Tutorials","Point"]
string1=""
print(string1.join(list1))
string2=" "
print(string2.join(list1))

Output
WelcomeToTutorialsPoint
Welcome To Tutorials Point'''