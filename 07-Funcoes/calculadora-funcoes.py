# Separar três operações matemáticas em funções pequenas.

def somar(primeiro, segundo):
    return primeiro + segundo


def subtrair(primeiro, segundo):
    return primeiro - segundo


def multiplicar(primeiro, segundo):
    return primeiro * segundo


numero1 = float(input('Digite o primeiro número: '))
numero2 = float(input('Digite o segundo número: '))

# Cada chamada usa os mesmos números, mas devolve o resultado da sua operação.
print('Soma:', somar(numero1, numero2))
print('Subtração:', subtrair(numero1, numero2))
print('Multiplicação:', multiplicar(numero1, numero2))
