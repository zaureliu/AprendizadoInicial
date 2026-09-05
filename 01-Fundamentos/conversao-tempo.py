# Separar uma quantidade de segundos em horas, minutos e segundos.

total = int(input('Digite uma quantidade inteira de segundos (zero ou mais): '))

# // calcula as horas completas e % pega os segundos que sobraram.
horas = total // 3600
restante = total % 3600
minutos = restante // 60
segundos = restante % 60

print('{} hora(s), {} minuto(s) e {} segundo(s).'.format(horas, minutos, segundos))
