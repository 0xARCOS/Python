def check_temperature(temp_str: str) -> int:
    try:
        temp = int(temp_str)
    except ValueError:
        raise ValueError(
            f"Caught input_temperature error: "
            f"invalid literal for int() with base 10: '{temp_str}'"
        )

    if temp > 40:
        raise ValueError(f"{temp}ºC is too hot for plants (max 40ºC)")
    if temp < 0:
        raise ValueError(f"{temp}ºC is too cold for plants (min 0ºC)")

    return temp


def test_temperature_input() -> None:
    print("=== Garden Temperature Checker ===")

    test_values = ["25", "abc", "100", "-50"]

    for value in test_values:
        print(f"\nTesting temperature: '{value}'")
        try:
            temp = check_temperature(value)
            print(f"Temperature is now {temp}ºC")
        except ValueError as e:
            print(f"{e}")

    print("\nAll tests completed - program didn't crash!")


if __name__ == "__main__":
    test_temperature_input()
