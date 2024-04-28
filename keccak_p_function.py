from step_mappings import *


def keccak_p(s: str, b, nr: int) -> str:
    if b not in (25, 50, 100, 200, 400, 800, 1600):
        raise Exception(f"You passed the wrong b, it cannot be equal to {b}")
    w = b // 25
    l = int(log2(w))

    state_array = np.array(np.zeros((5, 5, w)), dtype=bool)
    for y in range(5):
        for x in range(5):
            for z in range(w):
                state_array[x, y, z] = bool(int(s[(w*5)*y + w*x + z]))

    for ir in range(12 + 2*l - nr, 12 + 2*l):
        state_array = theta(state_array, b)
        state_array = rho(state_array, b)
        state_array = pi(state_array, b)
        state_array = hi(state_array, b)
        state_array = iota(state_array, b, ir)

    news = ""
    for y in range(5):
        for x in range(5):
            for z in range(w):
                news += str(int(state_array[x, y, z]))

    return news

