import random
from typing import Any, NoReturn
from collections.abc import Generator


PLAYERS: list[str] = ["alice", "bob", "charlie", "dylan"]
ACTIONS: list[str] = [
    "run",
    "eat",
    "sleep",
    "grab",
    "move",
    "climb",
    "swim",
    "use",
    "release"
    ]


def gen_event() -> Generator[tuple[str, str], Any, NoReturn]:
    while True:
        name: str = random.choice(seq=PLAYERS)
        action: str = random.choice(seq=ACTIONS)
        yield name, action


def consume_event(events: list[tuple[str, str]]) -> Generator[Any, Any, None]:
    while events:
        event: Any = random.choice(seq=events)
        events.remove(event)
        yield event


if __name__ == "__main__":
    stream: Generator[tuple[str, str], Any, NoReturn] = gen_event()

    print("=== Game Data Stream Processor ===")
    for _ in range(1000):
        name, action = next(stream)
        print(f"Event {_}: Player {name} did action {action}")

    stream2: Generator[tuple[str, str], Any, NoReturn] = gen_event()
    event_list: list[tuple[str, str]] = [next(stream2) for _ in range(10)]
    print(f"\nBuilt list of {len(event_list)} event: {event_list}")

    for event in consume_event(events=event_list):
        print(f"Got event from list: {event}")
        print(f"Remains in list: {event_list}")
