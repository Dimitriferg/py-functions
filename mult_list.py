from math import prod


def mult_list(numbers):
    product = 1
    for number in numbers:
        product = product * number
        return product



list = [2, 4, 6, 8]

print(mult_list(list))