#par ou impar
num = int(input('Me diga um número qualquer: '))
resto = num % 2
if resto == 0:
    print(f'O número {num} é PAR')
else:
    print(f'O número {num} é ÍMPAR')