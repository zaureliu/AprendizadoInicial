# Descobrir se um número inteiro é par ou ímpar.

numero = int(input('Digite um número inteiro: '))

# O operador % retorna o resto da divisão. Um número par tem resto zero por 2.
if numero % 2 == 0:
    print('O número é par.')
else:
    print('O número é ímpar.')
