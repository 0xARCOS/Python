from ex1 import HealingCreatureFactory, TransformCreatureFactory
from ex1.capability import HealCapability, TransformCapability


def test_healing() -> None:
    print("Testing Creature with healing capability")
    factory = HealingCreatureFactory()

    # Base
    print("base:")
    c_base = factory.create_base()
    assert isinstance(c_base, HealCapability)
    print(c_base.describe())
    print(c_base.attack())
    print(c_base.heal())

    # Evolved
    print("evolved:")
    c_evolved = factory.create_evolved()
    assert isinstance(c_evolved, HealCapability)
    print(c_evolved.describe())
    print(c_evolved.attack())
    print(c_evolved.heal())


def test_transform() -> None:
    print("\nTesting Creature with transform capability")
    factory = TransformCreatureFactory()

    # Base
    print("base:")
    c_base = factory.create_base()
    assert isinstance(c_base, TransformCapability)
    print(c_base.describe())
    print(c_base.attack())
    print(c_base.transform())
    print(c_base.attack())
    print(c_base.revert())

    # Evolved
    print("evolved:")
    c_evolved = factory.create_evolved()
    assert isinstance(c_evolved, TransformCapability)
    print(c_evolved.describe())
    print(c_evolved.attack())
    print(c_evolved.transform())
    print(c_evolved.attack())
    print(c_evolved.revert())


if __name__ == "__main__":
    test_healing()
    test_transform()
