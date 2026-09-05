# Contar de 1 até 10 e depois de 10 até 1.

print('Contagem crescente:')
# O último valor do range não entra na contagem.
for numero in range(1, 11):
    print(numero)

print('Contagem decrescente:')
# O passo -1 faz o contador diminuir a cada repetição.
for numero in range(10, 0, -1):
    print(numero)
