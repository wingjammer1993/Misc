import numpy as np
import random

SWAP = 30
SUB = 10
INDEL = 1

# Del = 1
# Insert = 2
# Sub = 3
# Swap = 4
# No-op = 5


def string_alignment(x, y):
    nx = len(x)+1
    ny = len(y)+1
    s = np.zeros((nx, ny))
    p = np.zeros((nx, ny))
    s[0][0] = 0
    p[0][0] = 0

    for i in range(0, nx):
        for j in range(0, ny):
            if i > 0 or j > 0:

                cost = list()

                if i > 0:
                    cost.append((s[i-1][j] + INDEL, 1))

                if j > 0:
                    cost.append((s[i][j-1] + INDEL, 2))

                if i > 1 and j > 1:
                    cost.append((s[i-2][j-2] + SWAP, 4))

                if i > 0 and j > 0:
                    if x[i-1] == y[j-1]:
                        cost.append((s[i-1][j-1], 5))
                    else:
                        cost.append((s[i-1][j-1] + SUB, 3))

                optimal = min(cost, key=lambda t: t[0])
                s[i][j] = optimal[0]
                p[i][j] = optimal[-1]
    return s, p


def extract_alignment(s, x, y):

    i = len(x)
    j = len(y)
    optimal_sequence = []

    while i > 0 or j > 0:

        valid_list = []

        if i-1 >= 0 and j-1 >= 0 and s[i][j] == s[i-1][j-1]:
            valid_list.append((i-1, j-1, 5, s[i-1][j-1]))

        if i-1 >= 0 and j >= 0 and s[i][j] - INDEL == s[i-1][j]:
            valid_list.append((i-1, j, 1, s[i-1][j]))

        if j-1 >= 0 and i >= 0 and s[i][j] - INDEL == s[i][j-1]:
            valid_list.append((i, j-1, 2, s[i][j-1]))

        if i-2 >= 0 and j-2 >= 0 and s[i][j] - SWAP == s[i-2][j-2]:
            valid_list.append((i-2, j-2, 4, s[i-2][j-2]))

        if i-1 >= 0 and j-1 >= 0 and s[i][j] - SUB == s[i-1][j-1]:
            valid_list.append((i-1, j-1, 3, s[i-1][j-1]))

        optimal = min(valid_list, key=lambda t: t[3])

        choice_list = []
        for elem in valid_list:
            if elem[3] == optimal[3]:
                choice_list.append(elem)

        current_vector = random.choice(choice_list)
        optimal_sequence.insert(0, current_vector[2])

        i = current_vector[0]
        j = current_vector[1]

    return optimal_sequence


def common_substrings(op_seq, length, x):

    common_strings = []
    substring = ""
    i = 0
    j = 0
    k = 0

    while i < len(x) and k < len(op_seq):

        if op_seq[k] == 5:
            substring += x[i]
            i += 1
            j += 1

        if op_seq[k] == 1:
            if len(substring) >= length:
                common_strings.append(substring)
                substring = ""
            i += 1

        if op_seq[k] == 2:
            if len(substring) >= length:
                common_strings.append(substring)
                substring = ""
            j += 1

        if op_seq[k] == 3:
            if len(substring) >= length:
                common_strings.append(substring)
                substring = ""
            i += 1
            j += 1

        if op_seq[k] == 4:
            if len(substring) >= length:
                common_strings.append(substring)
                substring = ""
            i += 2
            j += 2

        k += 1
    return common_strings


if __name__ == "__main__":

    with open('csci3104_F2017_PS7_data_string_x.txt') as read_x:
        x1 = read_x.read()

    with open('csci3104_F2017_PS7_data_string_y.txt') as read_y:
        y1 = read_y.read()

    # x1 = 'EXPONENTIAL'
    # y1 = 'POLYNOMIAL'
    lg = 242
    op_cost, backtrack = string_alignment(x1, y1)
    optimum = extract_alignment(op_cost, x1, y1)
    common = common_substrings(optimum, lg, x1)
    print(common)





