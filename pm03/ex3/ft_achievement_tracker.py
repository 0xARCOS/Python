import random

ACHIEVEMENTS: list[str] = [
    'First Steps', 'Boss Slayer', 'Treasure Hunter', 'Speed Runner',
    'Master Explorer', 'Collector Supreme', 'World Savior', 'Untouchable',
    'Crafting Genius', 'Strategist', 'Survivor', 'Unstoppable',
    'Sharp Mind', 'Hidden Path Finder'
]


def gen_player_achievements() -> set[str]:
    count: int = random.randint(a=1, b=len(ACHIEVEMENTS) - 2)
    return set(random.sample(ACHIEVEMENTS, count))


def main() -> None:
    alice: set = gen_player_achievements()
    bob: set = gen_player_achievements()
    charlie: set = gen_player_achievements()
    dylan: set = gen_player_achievements()

    print("=== Achievement Tracker System ===")
    print(f"Player Alice: {alice}")
    print(f"Player Bob: {bob}")
    print(f"Player Charlie: {charlie}")
    print(f"Player Dylan: {dylan}")

    all_distinct: set = set.union(alice, bob, charlie, dylan)
    print(f"All distinct achievements: {all_distinct}")

    common: set = set.intersection(alice, bob, charlie, dylan)
    print(f"Common achievements: {common}")

    others_a: set = set.union(bob, charlie, dylan)
    others_b: set = set.union(alice, charlie, dylan)
    others_c: set = set.union(alice, bob, dylan)
    others_d: set = set.union(alice, bob, charlie)

    print(f"Only Alice has: {set.difference(alice, others_a)}")
    print(f"Only Bob has: {set.difference(bob, others_b)}")
    print(f"Only Charlie has: {set.difference(charlie, others_c)}")
    print(f"Only Dylan has: {set.difference(dylan, others_d)}")

    print(f"Alice is missing: {set.difference(all_distinct, alice)}")
    print(f"Bob is missing: {set.difference(all_distinct, bob)}")
    print(f"Charlie is missing: {set.difference(all_distinct, charlie)}")
    print(f"Dylan is missing: {set.difference(all_distinct, dylan)}")


if __name__ == "__main__":
    main()
