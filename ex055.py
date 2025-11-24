#peso maior e peso menor
peso_maior = 0
peso_menor = 0

for c in range(1, 6):
    peso = float(input(f'Informe o peso da {c}. pessoa: '))
    if peso_menor == 0:
        peso_menor = peso
    elif peso_menor >= peso:
        peso_menor = peso    
    elif peso > peso_maior:
        peso_maior = peso

print(f'O menor peso foi: {peso_menor}Kg')
print(f'O maior peso foi: {peso_maior}Kg')
