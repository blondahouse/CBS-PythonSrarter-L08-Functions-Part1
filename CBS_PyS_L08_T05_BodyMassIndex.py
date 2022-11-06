def float_positive(message):
    while True:
        c = input(message)
        if c == 'off':
            exit()
        try:
            if float(c) <= 0:
                raise ValueError
        except ValueError:
            print("\t\tError message: Wrong input, try again")
        else:
            return float(c)


def bmi(height, weight):
    if weight/(height ** 2) < 18.5:
        print(f'\t\tYour body mass index is {weight/(height ** 2)} - you are underweight.\n')
    elif 18.5 <= weight/(height ** 2) < 25:
        print(f'\t\tYour body mass index is {weight/(height ** 2)} - you are normal.\n')
    else:
        print(f'\t\tYour body mass index is {weight/(height ** 2)} - you are overweight.\n')


while True:
    height = float_positive('\tEnter your height in meters, \'off\' to exit: ')
    weight = float_positive('\tEnter your weight in kilograms, \'off\' to exit: ')
    bmi(height, weight)
