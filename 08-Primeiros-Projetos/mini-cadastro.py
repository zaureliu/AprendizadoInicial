# Cadastrar e listar nomes fictícios, guardados somente enquanto o programa roda.

nomes = []

while True:
    print('\n1 - Cadastrar nome | 2 - Listar nomes | 0 - Sair')
    opcao = input('Escolha uma opção: ').strip()

    if opcao == '1':
        nome = input('Digite um nome fictício: ').strip()
        if nome == '':
            print('O nome não pode ficar vazio.')
        else:
            nomes.append(nome)
            print('Nome cadastrado.')
    elif opcao == '2':
        if len(nomes) == 0:
            print('Nenhum nome cadastrado.')
        else:
            # Percorremos a lista para mostrar um nome por linha.
            print('Nomes cadastrados:')
            for nome in nomes:
                print('-', nome)
    elif opcao == '0':
        print('Programa encerrado. Os nomes não foram salvos em arquivo.')
        break
    else:
        print('Opção inválida. Escolha um número do menu.')
