# Adivinhar um número de 1 a 10 em até três tentativas.

# random faz parte do Python; randint sorteia incluindo os dois limites.
from random import randint

sorteado = randint(1, 10)
acertou = False

for tentativa in range(1, 4):
    palpite = int(input('Tentativa {}: digite um inteiro de 1 a 10: '.format(tentativa)))

    if palpite == sorteado:
        print('Você acertou!')
        acertou = True
        # break encerra o laço assim que o jogador acerta.
        break
    elif palpite < 1 or palpite > 10:
        print('Palpite fora do intervalo. Esta tentativa foi usada.')
    elif palpite < sorteado:
        print('O número sorteado é maior.')
    else:
        print('O número sorteado é menor.')

if not acertou:
    print('As tentativas acabaram. O número era {}.'.format(sorteado))
