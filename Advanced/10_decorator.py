
# Exemplo de aplicação de decorator
#
# Este arquivo mostra duas coisas:
# 1) Um decorator simples que funciona com funções que aceitam
#    parâmetros (usando *args, **kwargs).
# 2) Um decorator parametrizável (factory) que recebe argumentos
#    quando é aplicado: @repetir(3).


def meu_decorador(func):
    """Decorator simples que envolve a execução de uma função.

    Usa *args e **kwargs para que a função decorada possa receber
    quaisquer parâmetros.
    """

    def wrapper(*args, **kwargs):
        print("Antes da função")
        result = func(*args, **kwargs)
        print("Depois da função")
        return result

    return wrapper


@meu_decorador
def funcao(param):
    print(f"Dentro da função, {param}.")


funcao(100)


# --- Decorator parametrizado (recebe argumento) ---

def repetir(n):
    """Decorator factory que repete a chamada da função N vezes.

    Uso:
        @repetir(3)
        def foo(...):
            ...

    O parâmetro ``n`` é passado ao aplicar o decorator e a função
    decorada é invocada `n` vezes.
    """

    def decorator(func):
        def wrapper(*args, **kwargs):
            resultado = None
            for i in range(n):
                print(f"Execução {i + 1}/{n}")
                resultado = func(*args, **kwargs)
            return resultado

        return wrapper

    return decorator


@repetir(3)
def diga_ola(nome):
    print(f"Olá, {nome}!")


diga_ola("Angelo")
