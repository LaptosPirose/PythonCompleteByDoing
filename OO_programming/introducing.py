class Student:
    """Represents a student with a name, school and a list of marks."""

    def __init__(self, name: str, school: str) -> None:
        self._name = name
        self._school = school
        self._marks: list[int] = []

    # -------------------------------------------
    # Properties
    # -------------------------------------------

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, value: str) -> None:
        if not isinstance(value, str):
            raise TypeError("Name must be a string.")
        self._name = value

    @property
    def school(self) -> str:
        return self._school

    @property
    def marks(self) -> list:
        """Return a copy to protect internal data."""
        return list(self._marks)

    # -------------------------------------------
    # Public API
    # -------------------------------------------

    def add_mark(self, value: int) -> None:
        if not isinstance(value, (int, float)):
            raise TypeError("Mark must be a number.")
        self._marks.append(value)

    def update_mark(self, index: int, value: int) -> None:
        if index < 0 or index >= len(self._marks):
            raise IndexError("Invalid mark index.")
        if not isinstance(value, (int, float)):
            raise TypeError("Mark must be a number.")
        self._marks[index] = value

    # -------------------------------------------
    # Representation
    # -------------------------------------------

    def __repr__(self) -> str:
        return f"Student(name={self._name!r}, school={self._school!r}, marks={self._marks!r})"

    def __str__(self) -> str:
        return f"Report for {self._name} ({len(self._marks)} marks)"


rolf = Student("Rolf Edward", "MIT")

rolf.name = "Rolf E."
print(rolf.name)

rolf.add_mark(100)
rolf.add_mark(90)
rolf.add_mark(80)

print(rolf.marks)
rolf.update_mark(0, 95)
print(rolf.marks)

print(rolf)       # str
print(repr(rolf))  # repr
rolf = Student("Rolf", "MIT")
print(rolf.__repr__())
print(rolf.__str__())
