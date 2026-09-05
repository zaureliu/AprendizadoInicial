# Converter uma velocidade de quilômetros por hora para metros por segundo.

quilometros_hora = float(input('Digite a velocidade em km/h (zero ou mais): '))

# Um quilômetro tem 1000 metros e uma hora tem 3600 segundos.
metros_segundo = quilometros_hora / 3.6

print('A velocidade é {:.2f} m/s.'.format(metros_segundo))
