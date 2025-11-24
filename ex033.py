#o menor e o maior valor digitado
print('\033[31m-=-\033[m' * 15)
n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
n3 = int(input('Terceiro valor: '))
print('\033[31m-=-\033[m' * 15)
#maior
if n1 >= n2:
    maior = n1
else:
    maior = n2
if maior <= n3:
    maior = n3
#menor
if n1 <= n2:
    menor = n1
else:
    menor = n2
if menor >= n3:
    menor = n3
print(f'O \033[33mmenor\033[m valor digitado foi: {menor}')
print(f'O \033[33mmaior\033[m valor digitado foi: {maior}')
print('\033[31m-=-\033[m' * 15)