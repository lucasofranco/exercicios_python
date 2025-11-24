#alistamento militar
ano = int(input('Em que ano você nasceu? '))

idade = 2025 - ano

print(f'Quem nasceu em {ano} tem {idade} ano(s) em 2025.')
if idade < 18:
    print('Você ainda vai se alistar no exército!')
    print(f'Falta {18 - idade} ano(s) para você se alistar.')
elif idade == 18:
    print(f'Já é a hora de você se alistar!')
elif idade > 18:
    print('Você já passou do prazo!')
    print(f'Você está atrasado {idade - 18} ano(s)!')
