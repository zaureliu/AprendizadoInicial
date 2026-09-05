# Encontrar o maior e o menor entre cinco números de uma lista.

numeros = []
for contador in range(1, 6):
    numero = float(input('Digite o número {}: '.format(contador)))
    numeros.append(numero)

# O primeiro item serve de ponto de partida, mesmo quando todos são negativos.
maior = numeros[0]
menor = numeros[0]
for numero in numeros:
    if numero > maior:
        maior = numero
    if numero < menor:
        menor = numero

print('O maior número é {} e o menor é {}.'.format(maior, menor))
