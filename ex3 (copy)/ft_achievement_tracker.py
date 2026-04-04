def main() -> None:
    alice = {'first_kill', 'level_10', 'treasure_hunter', 'speed_demon'}
    bob = {'first_kill', 'level_10', 'boss_slayer', 'collector'}
    charlie = {
        'level_10',
        'treasure_hunter',
        'boss_slayer',
        'speed_demon',
        'perfectionist'
    }

    print("=== Achivement Tracker System ===")
    print(f"Player alice achievements: {alice}")
    print(f"Player bob achievements: {bob}")
    print(f"Player charlie achievements: {charlie}")

    print("\n=== Achivement Analytics ===")
    print(f"All unique achievements: {alice | bob | charlie}")
    unique_achivement = alice | bob | charlie
    print(f"Total unique achievements: {len(unique_achivement)}")

    print(f"\nCommon to all players: {alice & bob & charlie}")
    rare_achievement = set()
    for achivement in unique_achivement:
        count = 0
        if achivement in alice:
            count += 1
        if achivement in bob:
            count += 1
        if achivement in charlie:
            count += 1
        if count == 1:
            rare_achievement.add(achivement)

    print(f"Rare achievements (1 player): {rare_achievement}")

    print(f"\nAlice vs Bob common: {alice & bob}")
    print(f"Alice unique: {alice - bob}")
    print(f"Bob unique: {bob - alice}")


if __name__ == "__main__":
    main()


jlkjlkjlk