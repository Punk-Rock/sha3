from sponge_function import *


def sha3_224_binary(binary_string: str):
    bit_digest = keccak_c(448, binary_string + '01', 224)
    return bit_digest

def sha3_224(m: str):
    bit_string = ''.join(format(ord(char), '08b') for char in m)

    digest = keccak_c(448, bit_string + '01', 224)

    return digest

def sha3_256(m: str):
    bit_string = ''.join(format(ord(char), '08b') for char in m)

    digest = keccak_c(512, bit_string + '01', 256)

    return digest

def sha3_384(m: str):
    bit_string = ''.join(format(ord(char), '08b') for char in m)

    digest = keccak_c(768, bit_string + '01', 384)

    return digest

def sha3_512(m: str):
    bit_string = ''.join(format(ord(char), '08b') for char in m)

    digest = keccak_c(1024, bit_string + '01', 512)

    return digest


