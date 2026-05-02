from ex0.creature import Creature
from abc import ABC, abstractmethod


class BattleStrategy(ABC):

    @abstractmethod
    def is_valid(self, creature: Creature) -> bool:
        pass
    
    @abstractmethod
    def act(self, creature: Creature) -> None:
        pass
