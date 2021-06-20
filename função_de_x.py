entrada = input()
data = entrada.split(' ')
x = float(data[2])

if x <= 1:
    fx = 1
if x > 1 and x <= 5:
    fx = x
if x > 5 and x <= 10:
    fx = x**2
if x > 10:
    fx = x**3

print('f(x) = ','{:.2f}'.format(fx))
# '{:.2f}'.format() gera numero com duas casa decimais