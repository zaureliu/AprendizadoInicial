#Exercicios para treinar operações matemáticas.
#Ordem de precedência:
# () parenteses
# ** exponenciação
# *, / , //, %
# + e -


n1 = int(input('Digite um valor: '))
n2 = int(input('digite um segundo valor: '))
soma  = n1 + n2     #Soma.
mult  = n1 * n2     #Multiplicação.     
div   = n1 / n2     #Divisão com resultado em decimal.
divint= n1 // n2    #Divisão com resultado inteiro.
exp1   = n1 ** n2   #Operação de exponenciação.

print('A soma é {}, a multiplicação é: {}, a divisão é: {}'.format(soma,mult,div))
print('A divisão inteira é: {}, a divisão em decimal é: {}, raiz quadrada é:{}'.format(divint, div, exp1))

#função format nas duas ultimas linhas pegam o resultado das variáveis e colocam nos colchetes apenas.