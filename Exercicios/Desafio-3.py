#Criar um algoritmo que pegue duas notas de um aluno e calcule sua média.abs



aluno=input('Nome do aluno: ')     
 #Pede informação ao usuário.

nota1=float(input('digite a primeira nota: '))   
#Pede informação ao usuário(aceita somente INTeiro).

nota2=float(input('digite a segunda nota: '))     
#Pede informação ao usuário(aceita somente INTeiro).

media=(nota1 + nota2)/2   
#Cálculo para saber a média.

print('A média do aluno(a)', aluno, 'é:', media )   
#Mostra as informações para usuário.
 

#Obs: / => divisão com número decimal no resultado.
#Obs2: // => divisão mostra apenas o resultado em numero inteiro, sem o 'resto'.