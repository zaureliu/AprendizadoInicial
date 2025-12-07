#Ler largura e altura de uma parede, e calcular sua area em m², em seguida a quantidade de tinta
#Cada L de tinta pinta 2m²



altura  = float(input("Qual a altura da parede? "))
#Solicita um valor

largura = float(input("Qual a largura da parede? "))   
#Solicita outro valor
     
area=(altura * largura)    
#Calcula área total da parede

totaltinta=(area/2)     
#Calcula quantidade de tinta necessária com o valor fixo 

print('A parede mede {}m² e a quantidade de tinta necessária é {:.2f} Litros'.format(area,totaltinta))      
#mostra na tela as informações necessárias
