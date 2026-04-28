import random

# Gera 15 números únicos entre 1 e 25
# O range(1, 26) inclui o 1 e vai até o 25
numeros = random.sample(range(1, 26), 15)

# Opcional: ordena os números para facilitar a leitura
numeros.sort()

print(f"Números gerados: {numeros}")
