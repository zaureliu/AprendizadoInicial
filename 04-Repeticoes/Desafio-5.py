#Pedir um numero de 1 a 9 e formar a tabuada inteira do mesmo.


numero = int(input('Qual tabuada você quer saber? '))   
#Atribui uma variável e insere um valor INTeiro.

print(f'tabuada do número:{numero}')       
#Mostrar qual tabuada o usuário escolheu.


for i in range(1,11):      
    #Função para repetir numa quantidade especifica uma determinada operação.

    total = numero * i     
    #Conforme o range escolhido, ele troca 'i' pela em ordem crescente de 1 até 10.

    print(f'{numero} x {i:2} = {total}')      
    #Mostra a informação(o range se aplica também aqui, mostrando de 1 até 10.)