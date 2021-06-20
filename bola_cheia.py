#Como descobrir o volume de bola de basquete pela circunferência dada

circ=float(input('A circunferência, em cm:',))
raio=circ/(2*3.1415)
vol=(raio**3)*3.1415*(4/3)
print('VOLUME = ',round(vol,2))