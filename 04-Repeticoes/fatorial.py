# Calcular o fatorial multiplicando os inteiros de 1 até o número escolhido.

numero = int(input('Digite um inteiro de 0 a 20: '))

if numero < 0 or numero > 20:
    print('Use um número de 0 a 20 neste exercício.')
else:
    # Começamos em 1 porque ele não altera a multiplicação. O fatorial de 0 é 1.
    fatorial = 1
    for fator in range(1, numero + 1):
        fatorial = fatorial * fator

    print('O fatorial de {} é {}.'.format(numero, fatorial))
