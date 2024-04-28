from keccak_p_function import *


def xor_string(s1: str, s2: str) -> str:
    if len(s1) != len(s2):
        raise Exception("LYS: s1 and s2 have different lengths")

    return "".join([str(int(s1[i] != s2[i])) for i in range(len(s1))])


def pad10_1(x: int, m: int):
    return "1" + "0" * ((-m - 2) % x) + "1"


def keccak_c(c, n_str, d):
    b = 1600
    r = b - c
    nr = 24

    p_str = n_str + pad10_1(r, len(n_str))
    n = len(p_str) // r

    s = '0' * b
    for i in range(n):
        s = keccak_p(xor_string(s, p_str[i * r:(i + 1) * r] + ('0' * c)), b, nr)

    z = ''
    z += s[:r]
    while len(z) < d:
        z += s[:r]
        s = keccak_p(s, b, nr)

    z = z[:d]
    result = ''
    for i in range(0, len(z), 8):
        bit_s2 = z[i:i+4]
        bit_s1 = z[i+4:i+8]
        s1 = str(hex(int(bit_s1[::-1], 2)))[2:]
        s2 = str(hex(int(bit_s2[::-1], 2)))[2:]
        result += s1 + s2

    return result


# def sponge(f, r: int, n_str: str, d: int, b: int) -> str:
#     p_str = n_str + pad10_1(r, len(n_str))
#     n = len(p_str) // r
#     c = b - r
#
#     s = '0' * b
#     for i in range(n):
#         s = f(xor_string(s, p_str[i*r:(i+1)*r]) + '0'*c, 1600, 24)
#
#     z = ''
#     while len(z) < d:
#         z += s[:r]
#         s = f(s, 1600, 24)
#
#     return z[:d]


