# Reaproveitar a verificação de paridade por meio de uma função.

def eh_par(numero):
    # return devolve o resultado para o trecho que chamou a função.
    return numero % 2 == 0


valor = int(input('Digite um número inteiro: '))
if eh_par(valor):
    print('O número é par.')
else:
    print('O número é ímpar.')
