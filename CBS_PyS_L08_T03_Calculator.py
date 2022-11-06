def my_menu(list_items):
    for index, value in enumerate(list_items):
        print(f'\t{index + 1}. {value}')
    print(f'\t0. Exit\n')


def dialogue(message, list_length):
    while True:
        c = input(message)
        try:
            range(list_length + 1).index(int(c))
        except ValueError:
            print("\t\tError message: Wrong input, try again")
        else:
            return int(c)


def int_in_range(message, range_left, range_right):
    while True:
        c = input(message)
        try:
            range(range_left, range_right + 1).index(int(c))
        except ValueError:
            print("\t\tError message: Wrong input, try again")
        else:
            return int(c)


def float_any(message):
    while True:
        c = input(message)
        try:
            float(c)
        except ValueError:
            print("\t\tError message: Wrong input, try again")
        else:
            return float(c)


def float_non_zero(message):
    while True:
        c = input(message)
        try:
            1/float(c)
        except ValueError:
            print("\t\tError message: Wrong input, try again")
        else:
            return float(c)


def addition():
    first_term = float_any('\tEnter first term (any float number): ')
    second_term = float_any('\tEnter second term (any float number): ')
    print(f'\t\t{first_term} + {second_term} = {first_term + second_term}\n')


def subtraction():
    first_term = float_any('\tEnter first term (any float number): ')
    second_term = float_any('\tEnter second term (any float number): ')
    print(f'\t\t{first_term} - {second_term} = {first_term - second_term}\n')


def multiplication():
    first_factor = float_any('\tEnter first factor (any float number): ')
    second_factor = float_any('\tEnter second factor (any float number): ')
    print(f'\t\t{first_factor} * {second_factor} = {first_factor * second_factor}\n')


def division():
    dividend = float_any('\tEnter dividend (any float number): ')
    divisor = float_non_zero('\tEnter divisor (non zero float number): ')
    print(f'\t\t{dividend} / {divisor} = {dividend / divisor}\n')


def exponentiation():
    base = float_any('\tEnter base (any float number): ')
    exponent = float_any('\tEnter exponent (any float number): ')
    print(f'\t\t{base} ^ {exponent} = {base ** exponent}\n')


def square_root():
    radicand = float_any('\tEnter base (any float number): ')
    degree = 1 / 2
    print(f'\t\tsquare root of {radicand} = {radicand ** degree}\n')


def cube_root():
    radicand = float_any('\tEnter base (any float number): ')
    degree = 1 / 3
    print(f'\t\tcube root of {radicand} = {radicand ** degree}\n')


list_items = ['addition',
              'subtraction',
              'multiplication',
              'division',
              'exponentiation',
              'square root',
              'cube root']

c = 1
while c:
    my_menu(list_items)
    c = dialogue('\tEnter action number (integer): ', len(list_items))
    match c:
        case 1:  # addition
            addition()
        case 2:  # subtraction
            subtraction()
        case 3:  # multiplication
            multiplication()
        case 4:  # division
            division()
        case 5:  # exponentiation
            exponentiation()
        case 6:  # square root
            square_root()
        case 7:  # cube root
            cube_root()
