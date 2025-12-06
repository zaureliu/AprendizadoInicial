#Pegar uma informação do usuário e fazer uma filtragem simples


dado = (input("Digite algo: "))

print('---Análise da informação inserida---')
print(f'Tipo primitivo: {type(dado)}')  #Função type sempre retornará string independente do que digite.

# filtro: Decimal? Numérico? Digito? Alfabético? Alfanumérico?
# está em maisúcula? Minúscula? Espaço?

print (f'É numérico? {dado.isnumeric()}')       #A função em colchetes vai indicar se a variavél é número (true or false).
print (f'é decimal? {dado.isdecimal()}')        #A função em colchetes vai indicar se a variavél é número decimal (true or false).
print (f'é digito? {dado.isdigit()}')           #A função em colchetes vai indicar se a variavél é um dígito (true or false).

print (f'É alfanumérico? {dado.isalnum()}')      #A função em colchetes vai indicar se a variavél é um alfanumérico (true or false).
print (f'É alfabético? {dado.isalpha()}')        #A função em colchetes vai indicar se a variavél é uma letra do alfabeto (true or false).

print (f'Está em maiúscula? {dado.isupper()}')   #A função em colchetes vai indicar se a variavél esta digitada toda em maiúsculo (true or false).
print (f'Está em minúscula? {dado.islower()}')   #A função em colchetes vai indicar se a variavél esta digitada toda em minúsculo (true or false).

print (f'É somente espaços? {dado.isspace()}')   #A função em colchetes vai indicar se a variavél contém somente espaços (true or false).
print (f'É simbolo? {dado.isascii()}')           #A função em colchetes vai indicar se a variavél é um caractere ASCII (true or false).
print (f'Está capitalizada? {dado.istitle()}')   #A função em colchetes vai indicar se a variavél está com a primeira letra maiúscula (true or false).

