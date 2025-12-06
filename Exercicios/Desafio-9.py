#Solicitar ao usuário o salário e informar o mesmo com 15% de aumento.abs



nome=input('Qual seu nome? ')
salario1=input(f'Bem vindo, {nome}! digite o seu salário mensal: ')
salario1=salario1.replace(',','.')
salario=float(salario1)

#Cálculo para descobrir a quantidade que irá aumentar
aumento=(salario*(15/100))

#Cálculo que irá fazer a soma do salário junto com 15% a mais
aumento1=(salario+aumento)


print(f'Olá {nome}, seu salário atual com aumento de 15% é: {aumento1}.')