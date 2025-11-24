#maior e menor valores
r = '' #resposta
tot = 0 #total de valores
menor = 0 #menor valor
maior = 0 #maior valor
s = 0 #soma dos valores

while r in ('S'):
    n = int(input('Digite um número: '))
    tot += 1
    s += n
    if menor == 0:
        menor = n
    elif menor >= n:
        menor = n
    elif n > maior:
        maior = n
    r = str(input('Quer continuar? [S/N] ')).upper().strip()[0]

print(f'Você digitou {tot} números e a média foi {s / tot:.2f}')
print(f'O maior valor foi {maior} e o menor foi {menor}.')
