def soma(x, y):
    return x + y


copia_soma = soma
print(copia_soma(3, 4))


def retorna_funcao():
    def imprime():
        print("Olá")
    return imprime

teste = retorna_funcao()
teste()

# Retorno de funções

def create_greet(name):
    def greet():
        print(f"HELOOOOO_! {name}.")
    return greet

victor_greet = create_greet("Victor")
victor_greet()

#