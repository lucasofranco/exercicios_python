#analisador completo
m = 0
maior_idade = 0
total_mulheres = 0

for c in range(1, 5):
    print(f'----- {c}. PESSOA -----')
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).upper().strip()
    if sexo == 'M':
        if idade > maior_idade:
            maior_idade = idade
            mais_velho = nome
    elif sexo == 'F':
        if idade < 20:
            total_mulheres = total_mulheres + 1
    m = m + (idade / 4) #calculo da media

print('-' * 15)
print(f'A média da idade do grupo é de {m} anos.')
print(f'O homem mais velho tem {maior_idade} anos e se chama {mais_velho.title()}.')
print(f'Ao todo são {total_mulheres} mulheres com menos de 20 anos.')
