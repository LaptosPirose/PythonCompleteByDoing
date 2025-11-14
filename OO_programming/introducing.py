import uuid
import logging
from dataclasses import dataclass, field
from typing import List, Dict, Any

# --------------------------------------
# Logging setup (isto normalmente fica em outro módulo)
# --------------------------------------
logger = logging.getLogger(__name__)


# --------------------------------------
# Domain Errors
# --------------------------------------
class StudentError(Exception):
    """Base error for Student domain operations."""


class InvalidNameError(StudentError):
    """Raised when a student receives an invalid name."""


class InvalidMarkError(StudentError):
    """Raised when an invalid mark is inserted or updated."""


# --------------------------------------
# Value Objects
# --------------------------------------
@dataclass(frozen=True)
class Mark:
    """Represents a validated student mark (0–100)."""

    value: float

    def __post_init__(self):
        if not (0 <= self.value <= 100):
            raise InvalidMarkError("Mark must be between 0 and 100.")


# --------------------------------------
# Entity
# --------------------------------------
@dataclass
class Student:
    """
    Enterprise-style Student entity.

    Characteristics:
    - Immutable ID.
    - Name and school may change, with validation.
    - Mark list encapsulated and validated.
    - Provides serialization helpers.
    - Separate errors and VOs.
    """

    # Immutable entity ID
    id: uuid.UUID = field(default_factory=uuid.uuid4, init=False)

    # Mutable attributes with validation
    _name: str = field(default="")
    _school: str = field(default="")
    _marks: List[Mark] = field(default_factory=list, repr=False)

    # --------------------------------------
    # Initialization
    # --------------------------------------
    def __init__(self, name: str, school: str) -> None:
        self.id = uuid.uuid4()
        self.set_name(name)
        self.set_school(school)
        self._marks: List[Mark] = []

        logger.debug(
            f"Student created: {self.id} | {self._name} | {self._school}")

    # --------------------------------------
    # Name
    # --------------------------------------
    @property
    def name(self) -> str:
        return self._name

    def set_name(self, name: str) -> None:
        if not isinstance(name, str) or not name.strip():
            raise InvalidNameError("Student name must be a non-empty string.")
        logger.info(f"Name updated for Student {self.id}: {name}")
        self._name = name.strip()

    # --------------------------------------
    # School
    # --------------------------------------
    @property
    def school(self) -> str:
        return self._school

    def set_school(self, school: str) -> None:
        if not isinstance(school, str) or not school.strip():
            raise InvalidNameError("School must be a non-empty string.")
        logger.info(f"School updated for Student {self.id}: {school}")
        self._school = school.strip()

    # --------------------------------------
    # Marks
    # --------------------------------------
    @property
    def marks(self) -> List[float]:
        """Return a read-only list of numeric mark values."""
        return [m.value for m in self._marks]

    def add_mark(self, value: float) -> None:
        mark = Mark(value)
        self._marks.append(mark)
        logger.info(f"Mark added for Student {self.id}: {value}")

    def update_mark(self, index: int, value: float) -> None:
        if index < 0 or index >= len(self._marks):
            raise InvalidMarkError("Invalid mark index.")
        self._marks[index] = Mark(value)
        logger.info(f"Mark updated for Student {self.id} at {index}: {value}")

    # --------------------------------------
    # Derived Data
    # --------------------------------------
    @property
    def average(self) -> float:
        """Compute student's average mark (0 if no marks)."""
        return round(sum(m.value for m in self._marks) / len(self._marks), 2) if self._marks else 0.0

    # --------------------------------------
    # Serialization
    # --------------------------------------
    def to_dict(self) -> Dict[str, Any]:
        """Convert entity to a serializable dictionary."""
        return {
            "id": str(self.id),
            "name": self._name,
            "school": self._school,
            "marks": self.marks,
            "average": self.average,
        }

    @staticmethod
    def from_dict(data: Dict[str, Any]) -> "Student":
        """Recreate entity from serialized data."""
        student = Student(name=data["name"], school=data["school"])
        student.id = uuid.UUID(data["id"])
        for m in data.get("marks", []):
            student.add_mark(m)
        return student

    # --------------------------------------
    # Technical Repr
    # --------------------------------------
    def __repr__(self) -> str:
        return (
            f"Student(id={self.id!s}, name={self._name!r}, "
            f"school={self._school!r}, marks={self.marks!r})"
        )


student = Student("Rolf Edward", "MIT")

student.add_mark(95)
student.add_mark(88)
student.update_mark(1, 91)

print(student.average)
print(student.to_dict())

data = student.to_dict()
clone = Student.from_dict(data)

print(clone)
