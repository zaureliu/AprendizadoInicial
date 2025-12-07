#Solicitar ao usuário o salário e informar o mesmo com 15% de aumento.abs



nome=input('Qual seu nome? ')       
#Solicita informação ao usuário.

salario1=float(input(f'Bem vindo, {nome}! digite o seu salário mensal: '))
#Mostra msg personalizada junto com outra informação solicitada.

aumento=(salario1*(15/100))
#Cálculo que irá descobrir valor exato a aumentar(porcentagem fixa).

aumento1=(salario1+aumento)
#Cálculo que irá fazer a soma do salário junto com 15% a mais.

print(f'Olá {nome}, seu salário atual com aumento de 15% é: {aumento1:.2f}.')
#Imprime na tela o nome do usuário e a informação processada.
# função após 'aumento1' limita quantidade de casas após virgula.