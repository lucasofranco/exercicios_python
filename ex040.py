#média
n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))

m = (n1 + n2) / 2

print(f'A média é: {m:.1f}')
if m < 5:
    print('Aluno reprovado!')
elif m >= 5 and m < 7:
    print('Aluno de recuperação')
else:
    print('Aluno aprovado!')
