#aprovando empréstimo

val = float(input('Valor da casa: R$'))
sal = float(input('Qual é o seu salário? R$'))
anos = int(input('Em quantos anos você pretende pagar? '))

prestacao = val / (anos * 12) #valor da prestacao
limite = sal * (30 / 100)

print(f'Para pagar uma casa de R${val:.2f} em {anos} anos a prestação será de R${prestacao:.2f}')

if prestacao <= limite:
    print('EMPRÉSTIMO APROVADO!')
else:
    print('EMPRÉSTIMO NEGADO!')
    