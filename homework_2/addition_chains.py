import random
from utils import convert_decimal_to_base


def left_to_right_binary(x, n, m):
    n_bin = bin(n)[2:]  # remove 0b from front
    k = len(n_bin)
    y = 1
    for i in range(0, k):
        y = pow(y, 2) % m
        if n_bin[i] == "1":
            y = (y * x) % m
    return int(y)


def left_to_right_fixed_window(x, n, m):
    beta = random.randint(3, 9)
    x_list = [1]

    for i in range(1, beta + 1):
        x_list.append(x_list[i - 1] * x % m)
    n_base_beta = convert_decimal_to_base(n, beta)
    k = len(n_base_beta)
    y = 1
    for i in range(0, k):
        y = pow(y, beta) % m
        y = y * x_list[n_base_beta[i]] % m
    return y


def left_to_right_sliding_window(x, n, m, w):
    x_list = [-1, x % m]
    x_list.append(x_list[1] * x_list[1] % m)

    for w in range(3, pow(2, w)):
        if w % 2 == 1:
            x_list.append(x_list[w - 2] * x_list[2] % m)
        else:
            x_list.append(-1)
    n_bin = convert_decimal_to_base(n, 2)
    y = 1
    k = len(n_bin)
    i = 0
    while i < k:
        if n_bin[i] == 0:
            y = y * y % m
            i = i - 1
        else:
            seq = longest_seq(n_bin, i, w)
            for l in range(1, len(seq) + 1):
                y = y * y % m
            x_seq = int("".join(str(integer) for integer in seq), 2)
            y = y * x_seq % m
            i = i + w - 1
    return y


def longest_seq(x, i, w):
    last_good_sequence = [x[i]]
    new_sequence = [x[i]]
    for j in range(i + 1, i + w):
        new_sequence.append(x[j])
        if int(x[j]) == 1:
            last_good_sequence = new_sequence.copy()
    return last_good_sequence


# print(longest_seq([1, 0, 0, 1, 1, 0, 0, 1], 3))


# print(left_to_right_binary(3, 5, 5))
# print(left_to_right_fixed_window(3, 10, 17))
# print(left_to_right_sliding_window(3, 4, 5, 3))
# x_seq = "".join(str(integer) for integer in [1, 0, 0])
# print(int(x_seq, 2))
