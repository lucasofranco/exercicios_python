#analisando triangulos 2.0
print('\033[33m-=-\033[m' * 15)
print('\033[36mAnalisador de Triângulos\033[m')
print('\033[33m-=-\033[m' * 15)

#colocando os segmentos
l1 = float(input('Primeiro segmento: '))
l2 = float(input('Segundo segmento: '))
l3 = float(input('Terceiro segmento: '))

print('\033[33m-=-\033[m' * 15)

#pode formar ou nao um triangulo?
if l1 < l2 + l3 and l2 < l1 + l3 and l3 < l1 + l2:
    print('Os segmentos acima \033[32mPODEM FORMAR\033[m um triângulo!')

    print('\033[33m-=-\033[m' * 15)
    print('\033[36mTipo de Triângulo:\033[m')
    print('\033[33m-=-\033[m' * 15)

    if l1 == l2 and l2 == l3:
        print('EQUILÁTERO: Todos os lados são iguais.')
    elif l1 != l2 != l3 != l1:
        print('ESCALENO: Todos os lados são diferentes.')
    else:
        print('ISÓSCELES: Dois lados são iguais e um é diferente.')
else:
    print('Os segmentos acima \033[31m NÃO PODEM FORMAR\033[m um triângulo!')

print('\033[33m-=-\033[m' * 15)
