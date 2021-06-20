numero=int(input())
#para inverter, um meio é transformar o int em str
numero=str(numero)
#fazendo: print('datatype',type(numero))
#tenho confirmação: datatype <class 'str'>
oremun=''.join(reversed(numero))
print(oremun)
#é algo como ".join reversed faz a reversão como itens de lista, e join serve pra juntar ela de volta em str"