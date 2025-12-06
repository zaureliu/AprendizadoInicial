#Solicitar ao usuário o salário e informar o mesmo com 15% de aumento.abs

nome=input('Qual seu nome? ')
salario_str=input(f'Bem vindo, {nome}! digite o seu salário mensal: ')
salario_str=salario_str.replace(',','.')
salario=salario_str(float)


print(f'Olá {nome}, seu salário autual é: {salario}.')