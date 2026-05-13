import time
from functools import wraps
from collections.abc import Callable


def spell_timer(func: Callable) -> Callable:
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Casting {func.__name__}...")
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        print(f"Spell completed in {end_time - start_time:.3f} seconds")
        return result
    return wrapper


def power_validator(min_power: int) -> Callable:
    def contador(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args, **kwargs):
            power = kwargs["power"] if "power" in kwargs else args[-1]
            if power >= min_power:
                return func(*args, **kwargs)
            return "Insufficient power for this spell"
        return wrapper
    return contador


def retry_spell(max_attempts: int) -> Callable:
    def decorador(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(1, max_attempts + 1):
                try:
                    return func(*args, **kwargs)
                except Exception:
                    if attempt < max_attempts:
                        print(
                            f"Spell failed, retrying..."
                            f" (attempt {attempt}/{max_attempts})"
                        )
            return f"Spell casting failed after {max_attempts} attempts"
        return wrapper
    return decorador


class MageGuild:
    @staticmethod
    def validate_mage_name(name: str) -> bool:
        return len(name) >= 3 and all(c.isalpha() or c.isspace() for c in name)

    @power_validator(min_power=10)
    def cast_spell(self, spell_name: str, power: int) -> str:
        return f"Successfully cast {spell_name} with {power} power"


@spell_timer
def fireball(target: str) -> str:
    time.sleep(0.1)
    return "Fireball cast!"


if __name__ == "__main__":
    guild = MageGuild()
    print(f"Nombre 'Ro': {guild.validate_mage_name('Ro')}")
    print(f"Nombre 'Merlín': {guild.validate_mage_name('Merlín')}")

    print(guild.cast_spell("Lightning", 5))
    print(guild.cast_spell("Lightning", 15))

    @retry_spell(max_attempts=3)
    def unstable_spell() -> str:
        raise Exception("Interferencia mística")

    print(unstable_spell())

    print("\nTesting spell timer...")
    result = fireball("Dragon")
    print(f"Result: {result}")
