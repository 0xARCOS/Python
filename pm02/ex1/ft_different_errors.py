def garden_operations() -> None:
    print("=== Garden Error Types Demo ===")

    GENERIC_ERRORS = (
        TypeError,
        ValueError,
        ZeroDivisionError,
        KeyError,
        FileNotFoundError,
    )

    print("\nTesting ValueError...")
    try:
        int("abc")
    except GENERIC_ERRORS as e:
        print(f"{e}")

    print("\nTesting ZeroDivisionError...")
    try:
        10 / 0
    except GENERIC_ERRORS as e:
        print(f"{e}")

    print("\nTesting FileNotFoundError...")
    try:
        open("missing.txt")
    except GENERIC_ERRORS as e:
        print(f"{e}")

    print("\nTesting KeyError...")
    try:
        plants = {"rose": 1, "tulip": 2}
        plants["missing_plant"]
    except GENERIC_ERRORS as e:
        print(f"Caught KeyError: {e}")

    print("\nTesting multiple errors together...")
    try:
        int("not_a_number")
    except (ValueError, ZeroDivisionError, FileNotFoundError, KeyError):
        print("Caught an error, but program continues!")


def test_error_types() -> None:
    garden_operations()
    print("\nAll error types tested successfully!")


if __name__ == "__main__":
    test_error_types()
