#dicionario em python
aluno = {}

aluno['nome'] = str(input('Nome: '))
aluno['media'] = float(input(f'Média de {aluno["nome"]}: '))

print(f'O nome do(a) aluno(a) é: {aluno["nome"]}')
print(f'A média é: {aluno["media"]}')

if aluno['media'] >= 7:
    print('Situação: APROVADO')
elif aluno['media'] >= 4 and aluno['media'] <= 6:
    print('Situação: RECUPERAÇãO')
else:
    print('Situação: REPROVADO')