#validando expressoes matematicas
expr = str(input('Digite a expressão: '))
pilha = []
for parent in expr:
    if parent == '(':
        pilha.append('(')
    elif parent == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
        
if len(pilha) == 0:
    print('Expressão válida')
else:
    print('Expressão válida')