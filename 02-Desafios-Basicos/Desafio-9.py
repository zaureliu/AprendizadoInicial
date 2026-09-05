#Solicitar ao usuário o salário e informar o mesmo com 15% de aumento.abs


nome=input('Qual seu nome? ')       
#Solicita informação ao usuário.

salario=float(input(f'Bem vindo, {nome}! digite o seu salário mensal: '))
#Mostra msg personalizada junto com outra informação solicitada.

aumento=salario + (salario*(15/100))
#Cálculo que irá descobrir valor exato a aumentar(porcentagem fixa).

print(f'Olá {nome}, seu salário atual com aumento de 15% é: {aumento:.2f}.')
#Imprime na tela o nome do usuário e a informação processada.
# função após 'aumento1' limita quantidade de casas após virgula.