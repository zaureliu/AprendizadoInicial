#Criar um algoritmo que peça um número ao usuário e mostre na tela o seu dobro, triplo e raiz quadrada.



numero=int(input('Digite um numero: '))     #Solicita ao usuário que digite um número, nesse caso apenas nº INTeiro.
dobro=(numero * 2)      #Atribuição de variável e operação de cálculo de multiplicação.
triplo=(numero * 3)     #Atribuição de variáve e operação de cálculo de multiplicação.
raiz=(numero ** 2)      #Atribuição de variável e operação de cálculo de exponenciação.

print('O dobro do numero é {}, o seu triplo é: {} e sua raiz quadarada é: {}. '.format(dobro,triplo,raiz))      #Mostra na tela o resultado.
                                                                               #format pega e insere as informações das variáveis nos colchetes, conforme ordem que colocar nos parênteses.
