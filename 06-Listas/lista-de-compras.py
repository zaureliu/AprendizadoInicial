# Montar uma lista de compras até o usuário digitar fim.

compras = []
item = input('Digite um produto ou fim para terminar: ').strip()

while item.lower() != 'fim':
    # Não adicionamos itens vazios à lista.
    if item != '':
        compras.append(item)
    item = input('Digite outro produto ou fim para terminar: ').strip()

if len(compras) == 0:
    print('A lista de compras está vazia.')
else:
    print('Lista de compras:')
    for produto in compras:
        print('-', produto)
