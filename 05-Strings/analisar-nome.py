# Mostrar um nome em maiúsculas e identificar a primeira e a última palavra.

nome = input('Digite um nome fictício completo: ').strip()

if nome == '':
    print('Nenhum nome foi digitado.')
else:
    # split separa o texto pelos espaços e devolve uma lista de palavras.
    palavras = nome.split()
    print('Nome em maiúsculas: {}'.format(nome.upper()))
    print('Quantidade de palavras: {}'.format(len(palavras)))

    # O índice 0 pega a primeira palavra e -1 pega a última.
    print('Primeira palavra: {}'.format(palavras[0]))
    print('Última palavra: {}'.format(palavras[-1]))
