# Procurar uma palavra inteira em uma frase sem pontuação.

frase = input('Digite uma frase sem pontuação: ').lower()
palavra = input('Qual palavra deseja procurar? ').strip().lower()

# split separa as palavras pelos espaços. A busca não diferencia maiúsculas.
palavras = frase.split()
if palavra == '' or len(palavra.split()) != 1:
    print('Digite uma única palavra para procurar.')
elif palavra in palavras:
    print('A palavra foi encontrada.')
else:
    print('A palavra não foi encontrada.')
