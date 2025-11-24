#valor do seno, cosseno e tangente de um ângulo
import math
an = float(input('Digite um ângulo: '))
sen = math.sin(math.radians(an))
cos = math.cos(math.radians(an))
tan = math.tan(math.radians(an))
print(f'O seno do ângulo {an}° é: {sen:.2f}')
print(f'O cosseno do ângulo {an}° é: {cos:.2f}')
print(f'A tangente do ângulo {an}° é: {tan:.2f}')