import time
import sys
import os

# Cores ANSI
verde = "\033[92m"
vermelho = "\033[91m"
amarelo = "\033[93m"
reset = "\033[0m"

os.system("cls" if os.name == "nt" else "clear")

arte = f"""
{verde}
FFFFF  EEEEE  L      I   ZZZZZ
F      E      L      I      Z
FFFF   EEEE   L      I     Z
F      E      L      I    Z
F      EEEEE  LLLLL  I   ZZZZZ

{vermelho}
N   N  AAAAA  TTTTT  AAAAA  L
NN  N  A   A    T    A   A  L
N N N  AAAAA    T    AAAAA  L
N  NN  A   A    T    A   A  L
N   N  A   A    T    A   A  LLLLL

{amarelo}✨ 🎄 FELIZ NATAL 🎄 ✨
{reset}
"""

# Efeito de digitação
for letra in arte:
    sys.stdout.write(letra)
    sys.stdout.flush()
    time.sleep(0.002)

# Piscar a frase final
for _ in range(6):
    time.sleep(0.5)
    print(f"\r{amarelo}✨ 🎄 FELIZ NATAL 🎄 ✨{reset}", end="")
    time.sleep(0.5)
    print("\r" + " " * 40, end="")
