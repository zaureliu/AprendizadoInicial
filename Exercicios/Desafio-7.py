#Ler largura e altura de uma parede, e calcular sua area em m², em seguida a quantidade de tinta
#Cada L de tinta pinta 2m²



altura  = input("Qual a altura da parede? ")     
#Solicita um valor

largura = input("Qual a largura da parede? ")     
#Solicita outro valor
altura = altura.replace(',','.')         
#substitui a virgula para ponto caso o usuário digite(py só entende valores com ponto).

largura = largura.replace(',','.')       
#substitui a virgula para ponto caso o usuário digite(py só entende valores com ponto).
largura = float(largura)      
#Converte para decimal em caso de número quebrado
altura = float(altura)   
#Converte para decimal em caso de número quebrado

area=(altura * largura)    
#Calcula área total da parede

totaltinta=(area/2)     
#Calcula quantidade de tinta necessária com o valor fixo 

print('A parede mede {}m² e a quantidade de tinta necessária é {} Litros'.format(area,totaltinta))      #mostra na tela as informações necessárias
