#aumento de salario
print('\033[34m-=-\033[m' * 15)
sal = float(input('Qual é o salário do funcionário? \033[32mR$\033[m'))
print('\033[34m-=-\033[m' * 15)
if sal <= 1250:
    sal_novo = sal + (sal * 15 / 100)
else:
    sal_novo = sal + (sal * 10 / 100)
print(f'Quem ganhava \033[32mR$\033[m{sal:.2f} passa a ganhar \033[32mR$\033[m{sal_novo:.2f} agora.')
print('\033[34m-=-\033[m' * 15)