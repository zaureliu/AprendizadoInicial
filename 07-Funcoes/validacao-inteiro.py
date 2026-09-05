# Pedir novamente a entrada até que seja possível convertê-la em inteiro.

def ler_inteiro(mensagem):
    while True:
        texto = input(mensagem)
        # try tenta a conversão. except trata o erro de um texto como 'abc'.
        try:
            numero = int(texto)
        except ValueError:
            print('Entrada inválida. Digite um número inteiro.')
        else:
            # return devolve o número e também encerra a função e seu laço.
            return numero


valor = ler_inteiro('Digite um número inteiro: ')
print('Você digitou {}.'.format(valor))
