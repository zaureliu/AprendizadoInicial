#Crie um algoritmo que leia a quantia em reais e converta em dólar.abs



carteira=float(input('Digite o valor que você tem na carteira: '))
dolar=(5.31)                #Cotação fixa do exercício, sem consulta ao valor atual.
conv=carteira / dolar
print('O saldo convertido com a cotação fixa do exercício é {:.2f} dólares.'.format(conv))

                        #comando para delimitar a 2 casas depois da virgula.
