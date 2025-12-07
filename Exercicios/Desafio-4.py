#Crie um algoritmo para pegar valor em metros e converta para centímetros e milímetros.


dado=(input('Digite o valor em metros(M): '))      
#Solicita info ao usuário.

dado=dado.replace(',','.')      
#Substitui virgula pelo ponto na str inserida.

dado = float(dado)      
#Converte a str em número decimal.

cm=(dado * 100)     #Cálculo de conversão.
mm=(dado * 1000)    #Cálculo de conversão.

print('A medida',dado,'m' ''' convertido para cm fica: {}cm e convertido para mm fica: {}mm''' .format(cm,mm)) 
#Insere na tela as informações já calculadas.
#format apenas pega as informações das variavéis e joga nos colchetes.