nome = input('diga seu nome:')
if('l' in nome[0:1]):
    #[0:1] é para a primeira letra apenas
 print('olá',nome,'!')
elif('t' in nome): 
 print('o que faz aqui',nome,'??')
else:
 print('sla entao')
 #atenção ao encadeamento de if, elif e else: elif e else voltarão para o inicio da linha