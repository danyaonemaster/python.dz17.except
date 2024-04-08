try:
    numbers = []
    while True:
        num = float(input("Enter additional number (or 0 to complete): "))
        if num == 0:
            break
        elif num < 0:
            raise ValueError("A number has been entered.")
        else:
            numbers.append(num)

    total = sum(numbers)
    print("Sum of additional numbers entered:", total)

except ValueError as e:
    print("Pardon:", e)
