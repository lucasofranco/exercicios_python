'''o ano é bissexto?'''
import datetime
print('\033[34m-=-\033[m' * 15)
print('\033[31mB\033[32mI\033[33mS\033[34mS\033[35m\033[36mE\033[37mX\033[31mT\033[32mO\033[m?')
print('\033[34m-=-\033[m' * 15)
ano = int(input('Que ano quer analisar? Coloque 0 para analisar o ano atual: '))
print('\033[34m-=-\033[m' * 15)
if ano == 0:
    ano = datetime.date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f'O ano {ano} é \033[32mBISSEXTO\033[m')
else:
    print(f'O ano {ano} \033[31mNÃO É BISSEXTO\033[m')