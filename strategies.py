from .base_strategy import BattleStrategy
from ex0.creature import Creature
from ex1.capability import HealCapability, TransformCapability


class NormalStrategy(BattleStrategy):
    def is_valid(self, creature: Creature) -> bool:
        return True
    
    def act(self, creature: Creature) -> None:
        print(creature.attack())


class AggressiveStrategy(BattleStrategy):
    def is_valid(self, creature: Creature) -> bool:
        return isinstance(creature, TransformCapability)
    
    def act(self, creature: Creature) -> None:
        if not self.is_valid(creature):
            raise InvalidBattleError(f"Invalid Creature '{creature._name}' for this aggresive strategy")
        print(creature.transform())
        print(creature.attack())
        print(creature.revert())


class DefensiveStrategy(BattleStrategy):
    def is_valid(self, creature: Creature) -> bool:
        return isinstance(creature, HealCapability)
    
    def act(self, creature: Creature) -> None:
        if not self.is_valid(creature):
            raise InvalidBattleError(f"Invalid Creature '{creature._name}' for this defensive strategy")
        print(creature.attack())
        print(creature.heal())
