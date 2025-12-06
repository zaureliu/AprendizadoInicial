#Pegar uma informação do usuário e fazer uma filtragem simples


dado = (input("Digite algo: "))

print('---Análise da informação inserida---')
print(f'Tipo primitivo: {type(dado)}')

# filtro: Decimal? Numérico? Digito? Alfabético? Alfanumérico?
# está em maisúcula? Minúscula? Espaço?

print (f'É numérico? {dado.isnumeric()}')
print (f'é decimal? {dado.isdecimal()}')
print (f'é digito? {dado.isdigit()}')

print (f'É alfanumérico? {dado.isalnum()}')
print (f'É alfabético? {dado.isalpha()}')

print (f'Está em maiúscula? {dado.isupper()}')
print (f'Está em minúscula? {dado.islower()}')

print (f'É somente espaços? {dado.isspace()}')
print (f'É simbolo? {dado.isascii()}') 
print (f'Está capitalizada? {dado.istitle()}')

