# Verificar se um ano positivo é bissexto pelo calendário gregoriano.

ano = int(input('Digite um ano positivo: '))

# Múltiplos de 100 só são bissextos quando também são múltiplos de 400.
if ano <= 0:
    print('Digite um ano maior que zero.')
elif ano % 400 == 0 or (ano % 4 == 0 and ano % 100 != 0):
    print('O ano é bissexto.')
else:
    print('O ano não é bissexto.')
