#sequencia de fibonacci
print('-' * 25)
print('Sequência de Fibonacci')
print('-' * 25)
n = int(input('Quantos termos você quer mostrar? '))

n1 = 0
n2 = 1
n3 = 0

print('=' * 25)
c = 0
while c < n:
    print(n3, end=' ')
    n1 = n2
    n2 = n3
    n3 = n1 + n2
    c += 1
print('ACABOU')
print('=' * 25)
