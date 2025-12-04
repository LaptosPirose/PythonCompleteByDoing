### Explicação do main.py

## from __future__ import annotations

Ele atrasa a avaliação das anotações de tipos (type hints) no momento em que o módulo é carregado.

Isso inclui tipos de retorno, tipos de parâmetros, tipos de atributos, tudo dentro de classes e funções.

🔍 Por que isso importa?

Sem esse atraso, o Python precisa resolver imediatamente cada anotação:

def get_user() -> User:
    ...

Então, no carregamento do módulo, o Python procura User já definido.
Se ainda não estiver definido (ou for circular), boom: NameError.

Com annotations, ele guarda isso como:

"User"

e só resolve mais tarde — quando alguma ferramenta (mypy, pydantic, IDE, etc.) realmente precisar daquele tipo.

👉 Pydantic é um porteiro

Ele valida quem tenta entrar no prédio e barra quem está irregular.

👉 Mypy é o engenheiro estrutural

Ele garante que o PRÉDIO não vai desmoronar.

Um não substitui o outro.

❌ Pydantic não substitui mypy
✔ Pydantic valida dados
✔ Mypy valida código

## import argparse

