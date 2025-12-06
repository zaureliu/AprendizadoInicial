#Ler largura e altura de uma parede, e calcular sua area em m², em seguida a quantidade de tinta
#Cada L de tinta pinta 2m²

altura  = input("Qual a altura da parede? ")
largura = input("Qual a largura da parede? ")
altura = altura.replace(',','.')
largura = largura.replace(',','.')
largura = float(largura)
altura = float(altura)

area=(altura * largura)

totaltinta=(area/2)

print('A parede mede {}m² e a quantidade de tinta necessária é {} Litros'.format(area,totaltinta))

