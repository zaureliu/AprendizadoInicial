# Guardar cinco valores em uma lista e calcular a média.

valores = []
for contador in range(1, 6):
    valor = float(input('Digite o valor {}: '.format(contador)))
    # append adiciona um valor ao final da lista.
    valores.append(valor)

total = 0
for valor in valores:
    total = total + valor

# len informa quantos valores foram guardados.
media = total / len(valores)
print('Valores digitados:', valores)
print('A média é {:.2f}.'.format(media))
