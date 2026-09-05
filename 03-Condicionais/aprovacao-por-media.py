# Calcular a média de duas notas e aplicar uma regra fictícia de aprovação.

nota1 = float(input('Digite a primeira nota (0 a 10): '))
nota2 = float(input('Digite a segunda nota (0 a 10): '))

# Só calculamos a situação quando as duas notas estão no intervalo esperado.
if nota1 < 0 or nota1 > 10 or nota2 < 0 or nota2 > 10:
    print('As notas devem estar entre 0 e 10.')
else:
    media = (nota1 + nota2) / 2
    print('A média é {:.2f}.'.format(media))

    # Neste exercício: 7 ou mais aprova; de 5 até menos de 7 fica em recuperação.
    if media >= 7:
        print('Aluno aprovado.')
    elif media >= 5:
        print('Aluno em recuperação.')
    else:
        print('Aluno reprovado.')
