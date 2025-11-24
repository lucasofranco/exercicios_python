#caixa eletronico
banco = 'BANCO LUKY'
print('=' * 30)
print(f'{banco:^29}')
print('=' * 30)

cin = vin = dez = um = 0

while True:
    try:
        valor_str = str(input('Qual valor você quer sacar? R$'))
        valor = int(valor_str)
        break
    except ValueError:
        print('Ops! Algo deu errado. Por favor, tente novamente!')
        print('-' * 30)

while True:
    if valor >= 50:
        valor -= 50
        cin += 1
    elif valor >= 20:
        valor -= 20
        vin += 1 
    elif valor >= 10:
        valor -= 10
        dez += 1
    elif valor >= 1:
        valor -= 1
        um += 1
    elif valor == 0:
        break 

print(f'Total de {cin} cédulas de R$50')   
print(f'Total de {vin} cédulas de R$20')  
print(f'Total de {dez} cédulas de R$10')  
print(f'Total de {um} moedas de R$1')
print('=' * 30)
print('VOLTE SEMPRE AO BANCO LUKY!')
