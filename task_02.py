try:
    numbers = input('enter numbers > 0 separator",": ')
    number_list = list(map(int, numbers.split(",")))

    match all(num >= 0 for num in number_list):
        case False:
            raise Exception
        case True:
            print(f"sum numbers: {sum(number_list)}")

except Exception:
    print('enter numbers > 0')
