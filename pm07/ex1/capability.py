from abc import ABC, abstractmethod


class HealCapability(ABC):
    @abstractmethod
    def heal(self, target: str = "itself") -> str:
        """Define la acción de curación."""
        pass


class TransformCapability(ABC):
    def __init__(self) -> None:
        self._transformed: bool = False

    @abstractmethod
    def transform(self) -> str:
        pass

    @abstractmethod
    def revert(self) -> str:
        pass
