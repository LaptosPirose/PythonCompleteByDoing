"""Import modules"""
import builtins

# Print built-in function.


def main():
    """" Main program."""
    print("#" * 100)
    print("""
    Na maioria das linguagens de programação, o que se aprende
    primeiro é mostrar algo na tela. Inclusive, existe um superstição
    que diz que o seu primeiro texto mostrado deve ser sempre o famoso
    'Hello World!'.
          """)

    print("""
    Print é uma 'built-in function', uma função interna do núcleo
    do Python e ele serve para mostrar informações na tela.

    A sintaxe para isso é:
        print(\"Hello World!\")

    A função print pode ter alguns parâmetros.
    Parâmetros são configurações que são passadas para a função
    que definem como ela vai executar sua tarefa.

    Quando você chama uma função, os valores de configuração são
    chamados de 'argumentos', e quando a função interpreta esses
    valores, são chamados de 'parâmetros'.

    Por exemplo, vejamos a função Print em sua definição:

    def print(
        *values: object,
        sep: str | None = " ",
        end: str | None = "\\n",
        file: _SupportsWriteAndFlush[str] | None = None,
        flush: bool
    ) -> None: ...

    A palavra chave 'def' é que marca a definição de uma função ou
    método. Dentro dos parênteses, temos os parâmetros configuráveis
    para essa função. Mas quando chamamos e configuramos a função
    print, chamamos isso de argumentos.

    Note que ela tem parâmetros como sep (Insere um caractere que
    separa as palavras) e end (Caractere que vai no final da execução
    do print).

    1. print(\"Hello World!\") # Sem parâmetros
    2. print(\"Hello World!\", \"sem parâmetros\") # Várias palavras sem parâmetros
    3. print(\"Hello World!\", \"com parâmetros\", sep = '-') # Várias palavras separadas por '-'
    # Várias palavras separadas
    4. print("4. Hello World!", "com parâmetros", sep='-', end='.')
    por '-' e terminada em '.'

    OBS.: Cuidado, ao usar o argumento end, ele não pula a linha, porque
    substitui o comportamento de pular a linha pelo caracter do argumento.


    Verificar se a função print está no módulo built in:
    5. print(print in builtins.__dict__.values())   # True

    Ou ainda:
    6. print(print.__module__)  # saída: 'builtins'

          """)
    print("#" * 100)
    print("""
    Aqui está, sequência, as saídas dos comandos:\n""")
    # Sem parâmetros
    print("1. Hello World!")
    # Várias palavras sem parâmetros
    print("2. Hello World!", "sem parâmetros")
    # Várias palavras separadas por '-'
    print("3. Hello World!", "com parâmetros", sep='-')
    # Várias palavras separadas por '-' e terminada em '.'
    print("4. Hello World!", "com parâmetros", sep='-', end='.')
    print("\n")

    print("Verificar se a função print está no módulo built in.")
    print("5. ", print in builtins.__dict__.values())   # True
    print("6. ", print.__module__)  # saída: 'builtins'

    print("#" * 100)


if __name__ == "__main__":
    main()
