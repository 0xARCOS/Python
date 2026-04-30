def ft_count_harvest_recursive():
    days = int(input("Days until harvest: "))

    def count_current(current):
        if current > days:
            return
        print(f"Days: {current}")
        if current == days:
            print("Harvest time!")
            return
        count_current(current + 1)

    count_current(1)
