def artifact_sorter(artifacts: list[dict]) -> list[dict]:
    """Ordena artefactos por orden descendente usando una lambda."""
    return sorted(artifacts, key=lambda x: x['power'], reverse=True)


def power_filter(mages: list[dict], min_power: int) -> list[dict]:
    """Filtra magos con poder mayor o igual a min_power usando filter()."""
    return list(filter(lambda mage: mage['power'] >= min_power, mages))


def spell_transformer(spells: list[str]) -> list[str]:
    """Transforma hechizos añadiendo prefijo y sufijo * usando map()."""
    return list(map(lambda name: f"* {name} *", spells))


def mage_stats(mages: list[dict]) -> dict[str, int | float]:
    """Devuelve max, min y promedio de poder de una lista de magos."""
    return {
        "max_power": max(mages, key=lambda m: m["power"])["power"],
        "min_power": min(mages, key=lambda m: m["power"])["power"],
        "avg_power": round(
            sum(m["power"] for m in mages) / len(mages), 2
        )
    }


if __name__ == "__main__":
    artifacts = [
        {'name': 'Crystal Orb', 'power': 85, 'type': 'Misc'},
        {'name': 'Fire Staff', 'power': 92, 'type': 'Weapon'}
    ]
    sorted_artifacts = artifact_sorter(artifacts)

    print("Testing artifact sorter...")
    first = sorted_artifacts[0]
    second = sorted_artifacts[1]
    print(
        f"{first['name']} ({first['power']} power) "
        f"comes before {second['name']} ({second['power']} power)"
    )

    spells = ["fireball", "heal", "shield"]
    transformed = spell_transformer(spells)
    print("\nTesting spell transformer...")
    print(" ".join(transformed))

    mages = [
        {'name': 'Alex', 'power': 80, 'element': 'Fire'},
        {'name': 'Jordan', 'power': 95, 'element': 'Water'},
        {'name': 'Riley', 'power': 70, 'element': 'Earth'}
    ]
    stats = mage_stats(mages)
    filtered = power_filter(mages, 90)

    print("\nTesting mage stats...")
    print(
        f"Max: {stats['max_power']}, "
        f"Min: {stats['min_power']}, "
        f"Avg: {stats['avg_power']}"
    )
    print(f"Mages with 90+ power: {[m['name'] for m in filtered]}")
