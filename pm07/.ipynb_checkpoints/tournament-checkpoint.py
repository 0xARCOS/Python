from ex0 import FlameFactory, AquaFactory
from ex1 import HealingCreatureFactory, TransformCreatureFactory
from ex2 import NormalStrategy, DefensiveStrategy, AggressiveStrategy
from ex2 import InvalidBattleError


def battle(opponents: list) -> None:
    print("*** Tournament ***")
    print(f"{len(opponents)} opponents involved")

    for i in range(len(opponents)):
        for j in range(i + 1, len(opponents)):
            factory1, strategy1 = opponents[i]
            factory2, strategy2 = opponents[j]

            creature1 = factory1.create_base()
            creature2 = factory2.create_base()

            print("\n* Battle *")
            print(creature1.describe())
            print(" vs. ")
            print(creature2.describe())
            print("now fight!")

            try:
                # código que puede fallar
                strategy1.act(creature1)
                strategy2.act(creature2)
            except InvalidBattleError as e:
                print(f"Battle error, aborting tournament: {e}")
                return


if __name__ == "__main__":

    flame_f = FlameFactory()
    aqua_f = AquaFactory()
    healing_f = HealingCreatureFactory()
    transform_f = TransformCreatureFactory()

    normal = NormalStrategy()
    defensive = DefensiveStrategy()
    aggressive = AggressiveStrategy()

    print("Tournament 0 (basic)")
    opponents = [(flame_f, normal), (healing_f, defensive)]
    print("[(flame_f, normal), (healing_f, defensive)]")
    battle(opponents)

    print("\nTournament 1 (error)")
    opponents = [(flame_f, aggressive), (healing_f, defensive)]
    print("[(flame_f, aggressive), (healing_f, defensive)]")
    battle(opponents)

    print("\nTournament 2 (multiple)")
    opponents = [(aqua_f, normal), (healing_f, defensive),
                 (transform_f, aggressive)]
    print("[(aqua_f, normal), (healing_f, defensive), \
    (transform_f, aggressive)]")
    battle(opponents)
