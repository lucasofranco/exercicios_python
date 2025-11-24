#progressao aritmetica 3.0

from time import sleep

print('----- 10 TERMOS DE UMA PA -----')
pt = int(input('Primeiro termo: '))
r = int(input('Razão: '))

tot_t = 0
c = 1
while c < 11:
    print(pt + (c - 1) * r, end=' ')
    ultimo = (pt + (c - 1) * r) 
    c += 1
    tot_t += 1
print('PAUSA')
pt = ultimo

t = 1
while t != 0:
    t = int(input('Quantos termos você quer mostrar a mais? '))
    c = 2
    while c < t + 2:
        print(pt + (c - 1) * r, end=' ')
        ultimo = (pt + (c - 1) * r)
        c += 1
        tot_t += 1
    pt = ultimo
    if t != 0:
        print('PAUSA')
    else:
        print('FINALIZANDO...')
        sleep(2)
    
print(f'Progressão finalizada com {tot_t} termos mostrados.')
