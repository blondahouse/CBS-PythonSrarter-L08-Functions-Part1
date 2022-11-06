def function1(*x):
    f1_results = []
    for n in x[0]:
        f1_results.append(n ** 2)
    return f1_results


def function2(*x):
    f2_results = []
    for n in x[0]:
        f2_results.append(round(n ** 0.5, 2)) if n >= 0 else f2_results.append('Error')
    return f2_results


list_values = [i * .5 for i in list(range(-10, 11))]
list_values_string = [str(i) + ' \t' for i in list_values]
print('\tf \\ x\t\t\t', "".join(list_values_string))

result1 = function1(list_values)
result1_string = [str(i) + ' \t' for i in result1]
print('f(x) = x^2\t\t\t', "".join(result1_string))

result2 = function2(list_values)
result2_string = [str(i) + ' \t' for i in result2]
print('f(x) = sqrt(2)\t\t', "".join(result2_string))
