#dividindo valores em várias listas
lista = []
pares = []
impares = []

print('-=' * 25)

while True:
    while True:
        try:
            v_str = str(input('Digite um valor: '))
            v = int(v_str)
            lista.append(v)
            break
        except ValueError:
            print('Ops! Algo deu errado! Tente novamente.')
    
    while True:
        r = str(input('Deseja continuar? [S/N] ')).upper().strip()[0]
        if r != 'S' and r != 'N':
            print('Ops! Algo deu errado! Tente novamente.')
        else:
            break
    if r == 'N':
        break

for valor in lista:
    if valor % 2 == 0:
        pares.append(valor)
    else:
        impares.append(valor)

print('-=' * 25)

print(f'A lista completa é: {lista}')
print(f'A lista de pares é: {pares}')
print(f'A lista de ímpares é: {impares}')