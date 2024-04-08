while True:
    try:
        print()
        name = input("Enter your name: ")
        age = int(input("Enter your age: "))
        if 0 >= age or age >= 130:
            raise Exception
        print(f"\nHello, {name}! Your age is {age}")
        break
    except Exception:
        print("\n enter 0 > age < 130")
