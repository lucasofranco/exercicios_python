#indice de massa corporal
peso = float(input('Qual o seu peso? (Kg) '))
alt = float(input('Qual a sua altura? (m) '))

if alt.is_integer():
    alt = alt
else:
    alt = alt / 100

IMC = peso / (alt**2)
print(f'O IMC dessa pessoa é de: {IMC:.1f}')

if IMC < 18.5:
    print('ATENÇÃO! Você está ABAIXO DO PESO.')
elif 18.5 <= IMC < 25:
    print('PARABÉNS! Você está na FAIXA IDEAL.')
elif IMC >= 25 and IMC <= 30:
    print('Você está em SOBREPESO.')
elif IMC >= 30 and IMC <= 40:
    print('ATENÇÃO! Você está OBESIDADE.')
elif IMC > 40:
    print('CUIDADO! Você está em OBESIDADE MÓRBIDA')
