#Pedir um numero de 1 a 9 e formar a tabuada inteira do mesmo.

numero = int(input('Qual tabuada você quer saber? '))
print(f'tabuada do número:{numero}')


for i in range(1,11):
    total = numero * i
    print(f'{numero} x {i}= {total}')  