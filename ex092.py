#cadastro de trabalhador em Python
from datetime import datetime
ano_atual = datetime.now().year
info = {}

info['nome'] = str(input('Nome: '))
ano_nasc = int(input('Ano de Nascimento: '))
idade = ano_atual - ano_nasc
info['idade'] = idade
ctps_v = int(input('Carteira de Trabalho (0 não tem): '))
info['ctps'] = ctps_v

if ctps_v != 0:

    info['contratação'] = int(input('Ano de Contratação: '))
    info['salário'] = float(input('Salário: R$'))

    ap = ano_atual - info['contratação'] #quanto tempo está trabalhando
    ap = 35 - ap #quanto anos faltam
    ap = idade + ap #idade que vai se aposentar
    info['aposentadoria'] = ap
    
    print('-=' * 25)
    for k, v in info.items():
        print(f'{k}: {v}')

else:
    print('-=' * 25)
    for k, v in info.items():
        print(f'{k}: {v}')