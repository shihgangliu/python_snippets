#!/bin/python3

"""There are some lines may exceed 79 characters
because I'm not sure the uniform specifications
"""


import math
import random
import sys


def number_prediction(numbers, is_long_recursive=False):
    """Predict next ten numbers for increasing integer sequence"""
    input_size = len(numbers)

    if input_size == 0:
        print("Must type one number for input")
        sys.exit(1)

    if input_size == 1:
        return [numbers[0] for _ in range(10)]

    result = []
    next_number = last_number = numbers[input_size-1]
    pre_last_number = numbers[input_size-2]

    sqrt_numbers = list(map(math.sqrt, numbers))
    is_all_sqrt_numbers = True
    for number in sqrt_numbers:
        if number.is_integer() is False:
            is_all_sqrt_numbers = False
            break

    if is_all_sqrt_numbers:
        next_numbers = number_prediction(list(map(int, sqrt_numbers)))
        for number in next_numbers:
            result.append(int(math.pow(number, 2)))
        return result

    if input_size == 2:
        if last_number % pre_last_number == 0:
            for _ in range(10):
                next_number *= (last_number / pre_last_number)
                result.append(int(next_number))
            return result
        else:
            for _ in range(10):
                next_number += (last_number - pre_last_number)
                result.append(int(next_number))
            return result

    if (last_number == pre_last_number * numbers[input_size-3] and
            (input_size == 3 or
                pre_last_number == numbers[input_size-3] * numbers[input_size-4])):
        for _ in range(10):
            next_number = last_number * pre_last_number
            pre_last_number = last_number
            last_number = next_number
            result.append(int(next_number))
        return result

    if (last_number == pre_last_number + numbers[input_size-3] and
            (input_size == 3 or
                pre_last_number == numbers[input_size-3] + numbers[input_size-4])):
        for _ in range(10):
            next_number = last_number + pre_last_number
            pre_last_number = last_number
            last_number = next_number
            result.append(int(next_number))
        return result

    if (last_number / pre_last_number
            == pre_last_number / numbers[input_size-3]):
        for _ in range(10):
            next_number *= (last_number / pre_last_number)
            result.append(int(next_number))
        return result

    if (last_number - pre_last_number
            == pre_last_number - numbers[input_size-3]):
        for _ in range(10):
            next_number += (last_number - pre_last_number)
            result.append(int(next_number))
        return result

    if is_long_recursive:
        return [random.randint(1, 10) for _ in range(10)]

    interval_numbers = []
    index = 1
    while index < input_size:
        interval_numbers.append(numbers[index] - numbers[index-1])
        index += 1

    next_interval_numbers = number_prediction(interval_numbers, True)
    for number in next_interval_numbers:
        next_number += number
        result.append(next_number)
    return result


if __name__ == '__main__':
    stdin = input()
    input_numbers = list(map(int, stdin.rstrip().split()))
    stdout = number_prediction(input_numbers)
    print(stdout)
