#tratando varios valores 1.0
n = s = t = 0
while n != 999:
    n = int(input('Digite um número [999 para parar]: '))
    if n != 999:
        s += n
        t += 1
print(f'Você digitou {t} números e a soma entre eles foi {s}.')
