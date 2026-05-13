from collections.abc import Callable, Sequence


def spell_combiner(
    spell1: Callable[[str, int], str],
    spell2: Callable[[str, int], str]
) -> Callable[[str, int], tuple[str, str]]:
    """Crea un hechizo que combina dos efectos en una tupla"""

    # Definimos la función interna (el "pergamino")
    def combined_spell(target: str, power: int) -> tuple[str, str]:
        res1 = spell1(target, power)
        res2 = spell2(target, power)
        return (res1, res2)  # Retornamos ambos resultados

    return combined_spell  # Entregamos ambos resultados


def power_amplifier(base_spell: Callable[[str, int], str],
                    multiplier: int) -> Callable[[str, int], str]:
    """
    Crea un hechizo potenciado que multiplica el poder antes de
    lanzarlo sobre el objetivo
    """
    # Esta es la "versión potenciada" que vamos a devolver
    def amplified_spell(target: str, power: int) -> str:
        # Multiplicamos el poder por el
        # multiplicador que capturamos en el exterior
        amplified_power = power * multiplier

        # Ejecutamos el hechizo original con el nuevo poder
        return base_spell(target, amplified_power)

    return amplified_spell


def conditional_caster(
    Condition: Callable[[str, int], bool],
    spell: Callable[[str, int], str]
) -> Callable[[str, int], str]:
    """
    Retorna un nuevo hechizo que solo se lanza si se cumple la condición.
    Si falla, el hechizo "fizzles" (se desvanece).
    """
    def wrapped_spell(target: str, power: int) -> str:
        # Primero evaluamos la condición con los mismos argumentos
        if Condition(target, power):
            return spell(target, power)

        # Si ls condición es False, retornamos el mensaje obligaatorio.
        return "Spell fizzled"

    return wrapped_spell


def spell_sequence(
    spells: Sequence[Callable[[str, int], str]]
) -> Callable[[str, int], list[str]]:
    """
    Retorna una función que lanza una ráfaga de hechizos en orden.
    Cada hechizo dde la lista recibe el mismo objetivo y poder.
    """

    def flurry(target: str, power: int) -> list[str]:
        # Usamos una lista por comprensión (list comprehension)
        return [spell(target, power) for spell in spells]

    return flurry


def fireball(target: str, power: int) -> str:
    """
    Hechizo básico de curación.
    """
    return f"Fireball hits {target} for {power} damage"


def heal(target: str, power: int) -> str:
    """
    Hechizo básico de curación.
    """
    return f"Heal restores {target} for {power} HP"


if __name__ == "__main__":
    target_dummy = "Dragon"
    base_power = 10

    # 1. Comprobamos el spell_combiner
    # Crea una función que lanza fuego y cura a la vez
    combined = spell_combiner(fireball, heal)
    res_comb = combined(target_dummy, base_power)
    print("Testing spell combiner...")
    print(f"Combined spell result: {res_comb[0]}, {res_comb[1]}")

    # 2. Prueba de power_amplifier
    # Triplicamos el poder base de la bola de fuego
    multiplier = 3
    mega_fireball = power_amplifier(fireball, multiplier)
    print("\nTesting power amplifier...")
    print(f"Original: {base_power}, Amplified: {base_power * multiplier}")
    print(f"Result: {mega_fireball(target_dummy, base_power)}")

    # 3. Prueba conditional_caster
    # Solo lanzamos si el poder es mayor a 20
    def strong_only(t: str, p: int) -> bool:
        return p > 20

    safe_spell = conditional_caster(strong_only, fireball)
    print("\nTesting conditional caster...")
    print(f"Power 10: {safe_spell(target_dummy, 10)}")  # Debe fallar
    print(f"Power 30: {safe_spell(target_dummy, 30)}")  # Debe ejecutarse

    # 4. Prueba de spell_sequence
    # Una ráfaga de tres hechizos seguidos
    grimoire = [fireball, heal, fireball]
    flurry = spell_sequence(grimoire)
    print("\nTesting spell sequence...")
    results = flurry(target_dummy, 15)
    for i, res in enumerate(results, 1):
        print(f"Sequence {i}: {res}")
