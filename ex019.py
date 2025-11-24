#sorteio para aluno apagar a lousa
import random
al1 = input('Nome do primeiro aluno: ')
al2 = input('Nome do segundo aluno: ')
al3 = input('Nome do terceiro aluno: ')
al4 = input('Nome do quarto aluno: ')
sorteado = random.choice([al1, al2, al3, al4])
print('=' * 20)
print(f'O aluno sorteado foi: {sorteado}')