#calcular comprimento hipotenusa
import math
cat_o = float(input('Cateto oposto: '))
cat_a = float(input('Cateto Adjacente: '))
hip = math.hypot(cat_o, cat_a)
print(f'O comprimento da hipotenusa é: {hip:.2f}')
