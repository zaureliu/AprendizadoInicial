# Verificar o formato de um IPv4. Este programa só analisa texto, sem usar a rede.

def ipv4_valido(endereco):
    partes = endereco.split('.')
    if len(partes) != 4:
        return False

    for parte in partes:
        # Cada parte deve ter de 1 a 3 dígitos ASCII; letras e sinais não entram.
        if len(parte) < 1 or len(parte) > 3:
            return False
        for caractere in parte:
            if caractere not in '0123456789':
                return False

        # Evitamos formas ambíguas como 001. O valor zero sozinho é aceito.
        if len(parte) > 1 and parte[0] == '0':
            return False
        if int(parte) > 255:
            return False

    return True


ip = input('Digite um IPv4 para analisar somente o formato: ').strip()
if ipv4_valido(ip):
    print('Formato IPv4 válido. Isso não informa se o endereço existe na rede.')
else:
    print('Formato IPv4 inválido. Use quatro números de 0 a 255 separados por pontos.')
