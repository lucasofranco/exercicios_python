#gerenciador de pagamentos
print(f'{" Lojas Lukynhas ":=^30}')
p = float(input('Preço das compras: R$'))
print('''FORMAS DE PAGAMENTOS
[ 1 ] à vista dinheiro/cheque)
[ 2 ] à vista cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão''')
op = int(input('Qual é a opção? '))

if op == 1:
    d = p - (p * 10 / 100)
    print(f'Sua compra de R${p} vai custar R${d:.2f} no final.')
elif op == 2:
    d = p - (p * 5 / 10)
    print(f'Sua compra de R${p} vai custar R${d:.2f} no final.')
elif op == 3:
    print(f'Sua compra de R${p} será parcelada em 2x de R${p / 2:.2f} SEM JUROS')
elif op == 4:
    par = int(input('Quantas parcelas? '))
    pf = p + (p *  20 / 100)
    print(f'Sua compra será parcelada em {par}x de R${(pf / par):.2f} COM JUROS') 
    print(f'Sua compra de R${p:.2f} vai custar R${pf:.2f} no final.')
else:
    print('\033[31mERRO!\033[m Selecione uma opção válida!')