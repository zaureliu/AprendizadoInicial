# Separar cinco números inteiros em duas listas.

pares = []
impares = []

for contador in range(1, 6):
    numero = int(input('Digite o inteiro {}: '.format(contador)))

    # Cada número é colocado na lista correspondente ao resto da divisão por 2.
    if numero % 2 == 0:
        pares.append(numero)
    else:
        impares.append(numero)

print('Números pares:', pares)
print('Números ímpares:', impares)
