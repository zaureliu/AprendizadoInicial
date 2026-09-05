# Criar funções para converter metros em centímetros e milímetros.

def metros_para_centimetros(metros):
    return metros * 100


def metros_para_milimetros(metros):
    return metros * 1000


medida = float(input('Digite uma medida em metros (zero ou mais): '))
if medida < 0:
    print('A medida não pode ser negativa.')
else:
    # A mesma medida é passada como argumento para as duas funções.
    print('Em centímetros: {}'.format(metros_para_centimetros(medida)))
    print('Em milímetros: {}'.format(metros_para_milimetros(medida)))
