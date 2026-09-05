# Converter uma temperatura de Celsius para Fahrenheit.

celsius = float(input('Digite a temperatura em Celsius: '))

# Primeiro multiplicamos por 9/5 e depois somamos 32.
fahrenheit = celsius * 9 / 5 + 32

print('A temperatura em Fahrenheit é {:.1f} °F.'.format(fahrenheit))
