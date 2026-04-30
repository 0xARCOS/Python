def ft_count_harvest_iterative():
    days = int(input("Days until harvest: "))
    for _ in range(1, days):
        print(f"Days: {_}")
    print("Harvest time!")
