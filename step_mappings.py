import numpy as np
from math import log2


def print_state_array(arr: np.array, b: int) -> None:
    counter = 0
    for y in range(5):
        for x in range(5):
            for i in range(0, b // 25, 8):
                bit_s2 = str(int(arr[x, y, i])) + str(int(arr[x, y, i + 1])) + str(int(arr[x, y, i + 2])) + str(int(arr[x, y, i + 3]))
                bit_s1 = str(int(arr[x, y, i + 4])) + str(int(arr[x, y, i + 5])) + str(int(arr[x, y, i + 6])) + str(int(arr[x, y, i + 7]))

                s1 = str(hex(int(bit_s1[::-1], 2)))[2:]
                s2 = str(hex(int(bit_s2[::-1], 2)))[2:]
                print(s1 + s2, end=' ')
                counter += 1

                if counter % 16 == 0:
                    print()
    print('\n\n$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$\n')


def theta(state_array: np.array, b: int) -> np.array:
    w = b // 25
    c = np.array(np.zeros((5, w)))

    for x in range(5):
        for z in range(w):
            c[x, z] = (int(state_array[x, 0, z]) + int(state_array[x, 1, z]) + int(state_array[x, 2, z]) +
                       int(state_array[x, 3, z]) + int(state_array[x, 4, z])) % 2

    d = np.array(np.zeros((5, w)), dtype=bool)
    for x in range(5):
        for z in range(w):
            d[x, z] = c[(x - 1) % 5, z] != c[(x + 1) % 5, (z - 1) % w]

    new_state_array = np.array(np.zeros((5, 5, w)), dtype=bool)
    for y in range(5):
        for x in range(5):
            for z in range(w):
                new_state_array[x, y, z] = state_array[x, y, z] != d[x, z]

    return new_state_array


def rho(state_array: np.array, b: int) -> np.array:
    w = b // 25

    new_state_array = state_array.copy()
    x, y = 1, 0
    for t in range(24):
        for z in range(w):
            new_state_array[x, y, z] = state_array[x, y, (z - int((t + 1) * (t + 2) * 0.5)) % w]
        x, y = y, (2 * x + 3 * y) % 5

    return new_state_array


def pi(state_array: np.array, b: int) -> np.array:
    w = b // 25

    new_state_array = np.array(np.zeros((5, 5, w)), dtype=bool)
    for y in range(5):
        for x in range(5):
            for z in range(w):
                new_state_array[x, y, z] = state_array[(x + (3 * y)) % 5, x, z]

    return new_state_array


def hi(state_array: np.array, b: int) -> np.array:
    w = b // 25

    new_state_array = np.array(np.zeros((5, 5, w)), dtype=bool)
    for y in range(5):
        for x in range(5):
            for z in range(w):
                new_state_array[x, y, z] = (state_array[x, y, z] !=
                                            ((not (state_array[(x + 1) % 5, y, z])) and state_array[(x + 2) % 5, y, z]))

    return new_state_array


def iota(state_array: np.array, b: int, ir: int) -> np.array:
    def rc(t: int) -> bool:
        if t % 255 == 0:
            return True

        r = [True, False, False, False, False, False, False, False]
        for i in range(1, (t % 255) + 1):
            r.insert(0, False)
            r[0] = r[0] != r[8]
            r[4] = r[4] != r[8]
            r[5] = r[5] != r[8]
            r[6] = r[6] != r[8]
            r = r[:8]

        return r[0]

    w = b // 25
    l = int(log2(w))
    new_state_array = state_array.copy()
    rc_array = [False] * w
    for j in range(l + 1):
        rc_array[2 ** j - 1] = rc(j + 7 * ir)
    for z in range(w):
        new_state_array[0, 0, z] = new_state_array[0, 0, z] != rc_array[z]

    return new_state_array
