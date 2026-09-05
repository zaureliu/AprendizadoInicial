# Juntar funções, condicionais e repetição em uma calculadora com menu.

def ler_numero(mensagem):
    while True:
        try:
            numero = float(input(mensagem))
        except ValueError:
            print('Digite um número válido; use ponto para a parte decimal.')
        else:
            return numero


def calcular(primeiro, segundo, operacao):
    if operacao == '1':
        return primeiro + segundo
    elif operacao == '2':
        return primeiro - segundo
    elif operacao == '3':
        return primeiro * segundo
    else:
        # O menu verifica o divisor antes de chamar esta função para dividir.
        return primeiro / segundo


while True:
    print('\n1 - Somar | 2 - Subtrair | 3 - Multiplicar | 4 - Dividir | 0 - Sair')
    opcao = input('Escolha uma opção: ').strip()

    if opcao == '0':
        print('Calculadora encerrada.')
        break
    elif opcao == '1' or opcao == '2' or opcao == '3' or opcao == '4':
        numero1 = ler_numero('Primeiro número: ')
        numero2 = ler_numero('Segundo número: ')

        if opcao == '4' and numero2 == 0:
            print('Não é possível dividir por zero.')
        else:
            resultado = calcular(numero1, numero2, opcao)
            print('Resultado: {}'.format(resultado))
    else:
        print('Opção inválida. Escolha um número do menu.')
