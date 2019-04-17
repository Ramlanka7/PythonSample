

def valid_number(number):
    try:
        int(number)
        return True
    except ValueError:
        return False


def add_numbers(numbers):
    x = 0
    for i in numbers:
        if valid_number(i):
            x = x + i
        else:
            return "Not a valid number"
    return x


def multiply_numbers(numbers):
    x = 1
    for i in numbers:
        if valid_number(i):
            x = x * i
        else:
            return "Not a valid number"
    return x


# print(add_numbers({3, 4, 5}))
# print(multiply_numbers({2, 0, 5}))

