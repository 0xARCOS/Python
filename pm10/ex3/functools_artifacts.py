from functools import reduce, partial, singledispatch
from collections.abc import Callable
from typing import Any
import functools
import operator


def spell_reducer(spells: list[int], operation: str) -> int:
    """
    Utiliza functools.reduce para combinar los poderes de una lista
    según la operación especificada (add, multiply, max, min).
    """
    if not spells:
        return 0

    ops = {
        "add": operator.add,
        "multiply": operator.mul,
        "max": lambda a, b: a if a > b else b,
        "min": lambda a, b: a if a < b else b,
    }

    if operation not in ops:
        raise ValueError(f"Operación desconocida: {operation}")

    return reduce(ops[operation], spells)


def partial_enchanter(
    base_enchantment: Callable[[int, str, str], str]
) -> dict[str, Callable[[str], str]]:
    """
    Usa functools.partial para crear 3 versiones especializadas de un hechizo.
    Fija el poder en 50 y predefine los elementos Fuego, Hielo y Rayo.
    """
    fire_enchant = partial(base_enchantment, 50, "Fire")
    ice_enchant = partial(base_enchantment, 50, "Ice")
    lightning_enchant = partial(base_enchantment, 50, "Lightning")

    return {
        "fire": fire_enchant,
        "ice": ice_enchant,
        "lightning": lightning_enchant
    }


@functools.lru_cache(maxsize=None)
def memoized_fibonacci(n: int) -> int:
    """
    Calcula el n-ésimo número de Fibonacci usando memoización.
    El decorador lru_cache evita recalcular valores ya conocidos.
    """
    if n < 2:
        return n

    return memoized_fibonacci(n - 1) + memoized_fibonacci(n - 2)


@singledispatch
def spell_dispatcher(spell: Any) -> str:
    """Función base: se ejecuta si el tipo de hechizo no es reconocido."""
    return "Unknown spell type"


@spell_dispatcher.register(int)
def _(spell: int) -> str:
    """Maneja hechizos de daño (enteros)."""
    return f"Damage spell: {spell} damage"


@spell_dispatcher.register(str)
def _(spell: str) -> str:
    """Maneja encantamientos (cadenas)."""
    return f"Enchantment: {spell}"


@spell_dispatcher.register(list)
def _(spell: list) -> str:
    """Maneja ráfagas de múltiples hechizos (listas)."""
    return f"Multi-cast: {len(spell)} spells"


if __name__ == "__main__":
    spells = [10, 20, 30, 40]

    print("Testing spell reducer...")
    print(f"Sum: {spell_reducer(spells, 'add')}")
    print(f"Product: {spell_reducer(spells, 'multiply')}")
    print(f"Max: {spell_reducer(spells, 'max')}")

    print("\nTesting memoized fibonacci...")
    print(f"Fib(0): {memoized_fibonacci(0)}")
    print(f"Fib(1): {memoized_fibonacci(1)}")
    print(f"Fib(10): {memoized_fibonacci(10)}")
    print(f"Fib(15): {memoized_fibonacci(15)}")

    print("\nTesting spell dispatcher...")
    print(spell_dispatcher(42))
    print(spell_dispatcher("fireball"))
    print(spell_dispatcher([1, 2, 3]))
    print(spell_dispatcher(3.14))
