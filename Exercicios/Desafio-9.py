#Solicitar ao usuário o salário e informar o mesmo com 15% de aumento.abs



nome=input('Qual seu nome? ')       
#Solicita informação ao usuário.

salario1=input(f'Bem vindo, {nome}! digite o seu salário mensal: ')
#Mostra msg personalizada junto com outra informação a ser inserida.

salario1=salario1.replace(',','.')
#alterar a virgula pelo ponto, caso for inserido.abs

salario=float(salario1)
#Conversão do valor em numero decimal, caso for inserido.

aumento=(salario*(15/100))
#Cálculo que irá descobrir valor que irá aumentar baseado no salário.

aumento1=(salario+aumento)
#Cálculo que irá fazer a soma do salário junto com 15% a mais

print(f'Olá {nome}, seu salário atual com aumento de 15% é: {aumento1}.')