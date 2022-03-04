# 53827876
"""
B. Ловкость рук
"""
def read_input():
    k = int(input())
    i = 4
    all_strings = []
    while i != 0:
        all_strings += [i for i in input() if i.isdigit()]
        i -= 1
    return k, all_strings


def hand_trainer(k, all_strings):
    dt = {}
    bonus = 0

    for i in range(len(all_strings)):
        dt[all_strings[i]] = dt.get(all_strings[i], 0) + 1

    for i in dt.values():
        if i <= 2 * k and i != 0:
            bonus += 1

    return bonus


if __name__ == '__main__':
    k, all_strings = read_input()
    print(hand_trainer(k, all_strings))
