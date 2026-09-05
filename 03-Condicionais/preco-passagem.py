# Calcular uma passagem com preços fictícios por quilômetro.

distancia = float(input('Digite a distância da viagem em km: '))

if distancia <= 0:
    print('A distância deve ser maior que zero.')
else:
    # A tarifa escolhida vale para toda a distância da viagem.
    if distancia <= 200:
        preco = distancia * 0.50
    else:
        preco = distancia * 0.45

    print('O preço da passagem neste exercício é R$ {:.2f}.'.format(preco))
