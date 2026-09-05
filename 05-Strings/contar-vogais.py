# Contar as vogais de um texto, incluindo as formas acentuadas abaixo.

texto = input('Digite um texto: ').lower()
quantidade = 0

# lower permite comparar letras sem separar maiúsculas e minúsculas.
for letra in texto:
    if letra in 'aeiouáàâãéêíóôõúü':
        quantidade = quantidade + 1

print('O texto tem {} vogal(is).'.format(quantidade))
