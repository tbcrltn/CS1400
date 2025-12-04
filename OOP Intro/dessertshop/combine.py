from typing import Protocol, runtime_checkable

@runtime_checkable
class Combineable(Protocol):
    
    def can_combine(self, other: "Combineable") -> bool:
        pass

    def combine(self, other: "Combineable") -> "Combineable":
        pass

