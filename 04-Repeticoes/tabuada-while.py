# Mostrar a tabuada de um número, agora usando while.

numero = int(input('Digite um número inteiro para ver a tabuada: '))
contador = 1

# A repetição continua enquanto o contador for menor ou igual a 10.
while contador <= 10:
    resultado = numero * contador
    print('{} x {} = {}'.format(numero, contador, resultado))
    # Atualizar o contador permite que o laço termine.
    contador = contador + 1
