#sistema de radar eletronico
v = float(input('Qual é a velocidade atual do carro? '))
if v > 80:
    print('MULTADO! Você excedeu o limite permitido que é de 80km/h.')
    m = (v - 80) * 7
    print(f'Você deve pagar uma multa de R${m:.2f}!')
print('Tenha um bom dia! Dirija com segurança!')