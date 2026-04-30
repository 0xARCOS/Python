import random

if __name__ == "__main__":
    print("=== Game Data Alchemist ===")

    players: list[str] = [
        'Alice', 'bob', 'Charlie', 'dylan', 'Emma',
        'Gregory', 'john', 'kevin', 'Liam'
    ]
    print(f"Initial list of players: {players}")

    capitalized_players: list[str] = [
        name.capitalize() for name in players
    ]
    print(f"New list with all names capitalized: {capitalized_players}")

    capitalized_only_one: list[str] = [
        name for name in players if name[0].isupper()
    ]
    print(f"New list of capitalized names only: {capitalized_only_one}")

    scores: dict[str, int] = {
        name: random.randint(a=0, b=1000) for name in capitalized_players
    }
    print(f"Score dict: {scores}")

    average: float = round(
        number=sum(scores.values()) / len(scores), ndigits=2
    )
    print(f"Score average is {average}")

    high_scores: dict[str, int] = {
        name: score for name, score in scores.items() if score > average
    }
    print(f"High scores: {high_scores}")
