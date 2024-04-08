def task_02_1(name, age):
    def format_greeting(name, age):
        if age < 0 or age > 130:
            raise ValueError("Invalid age")
        return f"Hello, {name}! Your age is {age}."

    try:
        message = format_greeting(name, age)
        print(message)
    except ValueError:
        print("\n enter 0 > age < 130")


def task_02_2(name, age):
    def format_greeting(name, age):
        try:
            if age < 0 or age > 130:
                raise ValueError
            return f"Hello, {name}! Your age is {age}."
        except ValueError:
            print("\n enter 0 > age < 130")

    try:
        message = format_greeting(name, age)
        print(message)
    except ValueError as e:
        print("\n enter 0 > age < 130")


name = input("Enter your name: ")
age = int(input("Enter your age: "))
