##Ler o preço de um produto e mostrá-lo com desconto de 5%



produto=input('Qual o produto? ')          
#Solicita o nome do produto
valor_str=input(f'Qual o valor de {produto}? ')     
#Solicita o valor do produto(ele mostra qual produto escolhi.)
valor_str=valor_str.replace(',','.')    
#Fazer a conversão caso o usuário digitar vírgula e entender como número.
valor=float(valor_str)          
#Converter a informação digitada em valor decimal.

desconto=(valor * (5/100))      #Operação para achar o valor de desconto.
desconto1=(valor - desconto)    #Operação para mostrar o valor com desconto.

print('o valor do(a) {} está custando {} R$ com 5%'' de desconto.'.format(produto,desconto1))        
#Mostrar para o usuário o produto escolhido com o valor com 5% de desconto.