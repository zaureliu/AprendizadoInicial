# Comparar três números, incluindo a possibilidade de valores iguais.

primeiro = float(input('Digite o primeiro número: '))
segundo = float(input('Digite o segundo número: '))
terceiro = float(input('Digite o terceiro número: '))

# Começamos com o primeiro e trocamos o maior quando encontramos outro acima dele.
maior = primeiro
if segundo > maior:
    maior = segundo
if terceiro > maior:
    maior = terceiro

print('O maior valor é {}.'.format(maior))
