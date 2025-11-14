from dataclasses import dataclass


@dataclass(frozen=True)
class Name:
    value: str

    def __post_init__(self):
        value = (self.value or "").strip()
        if not value:
            raise ValueError("Name must not be empty.")
        if len(value) < 2:
            raise ValueError("Name too short.")
        # exemplo de validação opcional:
        if any(char.isdigit() for char in value):
            raise ValueError("Name must not contain numbers.")
        # normaliza o valor
        object.__setattr__(self, "value", value)


Name("Rolf Edward")    # ok
print(Name)
# Name(" ")              # deve lançar ValueError
# Name("A")              # deve lançar ValueError (curto demais)
# Name("João3")          # deve lançar ValueError (número)
