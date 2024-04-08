def task_04_1():
    def calculate_sum(numbers):
        return sum(numbers)

    try:
        numbers = []
        while True:
            num = float(input("Enter a positive number (or 0 to finish): "))
            if num == 0:
                break
            elif num < 0:
                raise ValueError("A negative number was entered.")
            else:
                numbers.append(num)

        total = calculate_sum(numbers)
        print("Sum of positive numbers entered:", total)

    except ValueError as e:
        print("Error:", e)


def task_04_2():
    def calculate_sum(numbers):
        try:
            if any(num < 0 for num in numbers):
                raise ValueError
            return sum(numbers)
        except ValueError:
            print("Negative number detected.")

    try:
        numbers = []
        while True:
            num = float(input("Enter a positive number (or 0 to finish): "))
            if num == 0:
                break
            else:
                numbers.append(num)

        total = calculate_sum(numbers)
        print("Sum of positive numbers entered:", total)

    except ValueError as e:
        print("Error:", e)

task_04_1()
task_04_2()