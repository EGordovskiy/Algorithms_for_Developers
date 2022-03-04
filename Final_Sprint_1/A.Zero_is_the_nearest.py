# 53790046
"""
A. Ближайший ноль

Необходимо рассчитать для каждого из участков расстояние до ближайшего нуля.
Числа выводятся в одну строку, разделясь пробелами.
"""
def read_input():
    street_length = int(input())
    house_numbers = list(map(int, input().split()))
    return street_length, house_numbers


def nearest_null(street_length, house_numbers):
    result = []

    for i in range(street_length):
        result.append(0)

    if house_numbers[0] == 0:
        result[0] = 0
    else:
        result[0] = 10 ** 9

    for i in range(1, street_length):
        if house_numbers[i] == 0:
            result[i] = 0
        else:
            result[i] = result[i - 1] + 1

    for i in range(street_length - 2, -1, -1):
        if house_numbers[i] == 0:
            result[i] = 0
        else:
            result[i] = min(result[i], result[i + 1] + 1)
    return result


if __name__ == '__main__':
    n, arr = read_input()
    print(" ".join(map(str, nearest_null(n, arr))))
