#Exercicios para treinar operações matemáticas
#Ordem de precedência:
# () parenteses
# ** exponenciação
# *, / , //, %
# + e -

n1 = int(input('Digite um valor: '))
n2 = int(input('digite um segundo valor: '))
soma  = n1 + n2
mult  = n1 * n2
div   = n1 / n2
divint= n1 // n2
exp1   = n1 ** n2

print('A soma é {}, a multiplicação é: {}, a divisão é: {}'.format(soma,mult,div))
print('A divisão inteira é: {}, a divisão em decimal é: {}, raiz quadrada é:{}'.format(divint, div, exp1))