#vários números com flag
tot = s = 0
while True:
    n = int(input('Digite um número (999 para parar): '))
    if n == 999:
        break
    s += n
    tot += 1
print(f'A soma dos {tot} valores foi {s}.')
