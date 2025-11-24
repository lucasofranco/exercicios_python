#
de_menor = 0
de_maior = 0

for c in range(1, 8):
    nasc = int(input(f'Em que ano a {c}. pessoa nasceu? '))
    idade = 2025 - nasc
    if idade >= 21:
        de_maior = de_maior + 1
    if idade <= 20:
        de_menor = de_menor + 1
        
print(f'{de_menor} pessoa(s) ainda é/são de menor.')
print(f'{de_maior} pessoa(s) já é/são de maior.')
