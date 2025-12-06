#Ler o preço de um produto e mostrá-lo com desconto de 5%.abs

produto=input('Qual o produto? ')          #solicita o nome do produto
valor_str=input(f'Qual o valor de {produto}? ')     #solicita o valor do produto(ele mostra qual produto escolhi.)
valor_str=valor_str.replace(',','.')    #Fazer a conversão caso o usuário digitar vírgula e entender como número.
valor=float(valor_str)          #converter a informação digitada em valor decimal.

desconto=(valor * (5/100))      #operação para achar o valor de desconto
desconto1=(valor - desconto)    #operação para mostrar o valor com desconto.

print('o valor do(a) {} está custando {} R$ com 5%'' de desconto.'.format(produto,desconto1))        #Mostrar para o usuário o produto escolhido com o valor com 5% de desconto.