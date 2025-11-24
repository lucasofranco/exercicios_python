#tipo primitivo e informações adicionais
print('=====INFORMAÇÕES=====')
n = input('Digite algo: ')
print(f'O tipo primitivo de {n} é:', type(n))
print(f'"{n}" é um número?', n.isnumeric())
print(f'"{n}" é tudo maiúsculo?', n.isupper())
print(f'"{n}" são apenas letras?', n.isalpha())
print(f'"{n}" é alfa númerico?', n.isalnum())
print(f'"{n}" só tem espaços?', n.isspace())