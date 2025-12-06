#Crie um algoritmo que leia a quantia em reais e converta em dólar.abs



carteira=(input('Digite o valor que você tem na carteira: '))
valor=float(carteira)             #float é para converter em número decimal.
dolar=(5.31)                      #aqui nao vai float, já defini valor fixo para a var.

conv=valor / dolar
print('O saldo convertido em dólar atualmente é {:.2f} dólares.'.format(conv))
 #                                                 ^
                                 #comando para delimitar a 2 casas depois da virgula.