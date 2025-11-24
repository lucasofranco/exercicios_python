#ordem de apresentação dos alunos
import random
print('=' * 30)
al1 = input('Primeiro aluno: ')
al2 = input('Segundo aluno: ')
al3 = input('Terceiro aluno: ')
al4 = input('Quarto aluno: ')
print('=' * 30)
lista = [al1, al2, al3, al4]
random.shuffle(lista)
print('Ordem de apresentação:', lista)