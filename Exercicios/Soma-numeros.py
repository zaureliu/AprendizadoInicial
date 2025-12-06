#Solicitar dois numeros ao usuários, somar e imprimir resultado.abs



n1=int(input('Digite um número: '))
n2=int(input('Digite um segundo número: '))
s=(n1+n2)

# print('A soma de',n1,'e',n2,'é:',s) (formato antigo)
print('A soma entre {} e {} vale {}'.format(n1,n2,s))


