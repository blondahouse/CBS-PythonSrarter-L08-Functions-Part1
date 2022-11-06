def arithmetic_mean(*numbers):
    if len(numbers[0]) == 0:
        print(f'\t\tarithmetic mean of empty input is 0\n')
        return
    print(f'\t\tarithmetic mean of {list(numbers[0])} is {sum(numbers[0]) / len(numbers[0])}\n')


while True:
    while True:
        c = input('\tEnter any numbers separated by a space, \'off\' to exit: ')
        if c == 'off':
            exit()
        try:
            c_set = c.split()
            for index, value in enumerate(c_set):
                c_set[index] = float(value)
            break
        except ValueError:
            print("\t\tError message: Wrong input, try again")

    arithmetic_mean(c_set)
