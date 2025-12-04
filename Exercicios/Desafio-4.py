#Crie um algoritmo para pegar um valor em metros e converta para centimetros e milimetros.abs

dado=(input('Digite o valor em metros(M): '))
dado=dado.replace(',','.')
dado = float(dado)

cm=(dado * 100)
mm=(dado * 1000)

print('A medida',dado, '''convertido para cm fica: {}cm e convertido para mm fica: {}mm''' .format(cm,mm))

#finalizado