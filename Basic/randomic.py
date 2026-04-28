import random

# Gera 15 floats aleatórios entre 1 e 200
numeros = [random.uniform(1, 200) for _ in range(15)]

# Opcional: ordena os números para facilitar a leitura
numeros.sort()

print(f"Floats gerados: {numeros}")

# Exemplo de um único float aleatório
single_float = random.uniform(1, 200)
print(f"Float único: {single_float}")
