# Somar os números pares de 1 até um limite informado.

limite = int(input('Somar os pares até qual inteiro positivo? '))
soma = 0

if limite < 1:
    print('O limite deve ser maior que zero.')
else:
    # A variável soma guarda o total acumulado durante o laço.
    for numero in range(1, limite + 1):
        if numero % 2 == 0:
            soma = soma + numero

    print('A soma dos pares é {}.'.format(soma))
