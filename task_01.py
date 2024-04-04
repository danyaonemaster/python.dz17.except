while True:
    try:
        print()
        name = input("Enter your name: ")
        age = int(input("Enter your age: "))
        if 0 >= age or age >= 130:
            raise Exception
        print(f"Hello, {name}! Your age is {age}")
        break
    except Exception:
        print("enter age 0 to 130")

