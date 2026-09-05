# Verificar se um texto fica igual quando lido de trás para frente.

texto = input('Digite uma palavra ou frase, sem pontuação: ')

# Neste exercício ignoramos espaços comuns e maiúsculas; os acentos continuam.
texto = texto.lower().replace(' ', '')
invertido = ''

# Colocar cada letra antes do resultado constrói o texto invertido.
for letra in texto:
    invertido = letra + invertido

if texto == '':
    print('Digite pelo menos uma letra.')
elif texto == invertido:
    print('O texto é um palíndromo.')
else:
    print('O texto não é um palíndromo.')
