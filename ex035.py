#forma um triangulo?
print('\033[33m-=-\033[m' * 15)
print('\033[36mAnalisador de Triângulos\033[m')
print('\033[33m-=-\033[m' * 15)
l1 = float(input('Primeiro segmento: '))
l2 = float(input('Segundo segmento: '))
l3 = float(input('Terceiro segmento: '))
print('\033[33m-=-\033[m' * 15)
if l1 < l2 + l3 and l2 < l1 + l3 and l3 < l1 + l2:
    print('Os segmentos acima \033[32mPODEM FORMAR\033[m um triângulo!')
else:
    print('Os segmentos acima \033[31mNÃO PODEM FORMAR\033[m um triângulo!')
print('\033[33m-=-\033[m' * 15)