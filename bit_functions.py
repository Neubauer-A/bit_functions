'''
1.  Find parity of 32-bit x.
2.  Mod x by a power of 2.
3.  Check if x is a power of two.
4.  Swap bits (e.g. '10101' becomes '11100' when we swap indices 0 and 3).
5.  Reverse order of 8 bits.
6.  Reverse order of 32 bits.
7.  Get number of 1s in binary of 32-bit x.
8   Get the closest int with the same weight as x.
'''

def parity(x):
    x ^= x >> 32
    x ^= x >> 16
    x ^= x >> 8
    x ^= x >> 4
    x ^= x >> 2
    x ^= x >> 1
    return x & 1

def propagate_right(x): #1
    return x | (x - 1)

def modulo(x, pow): #2
    return x & (pow-1)

def is_pow_2(s): #3
    x &= (x-1)
    return True if not x else False

def bitswap(x, i, j): #4
    if (x >> i) & 1 != (x >> j) & 1:
        x ^= (1 << i)
        x ^= (1 << j)
    return x

def reverse_8(x): #5
    x = bitswap(x, 0, 7)
    x = bitswap(x, 1, 6)
    x = bitswap(x, 2, 5)
    x = bitswap(x, 3, 4)
    return x

def reverse_32(x): #6
    cache = {}
    for n in range(256):
        cache[n] = reverse_8(n)

    mask = (2**8)-1
    return (cache[x & mask] << 24) | \
    (cache[(x >> 8) & mask] << 16) | \
    (cache[(x >> 16) & mask] << 8) | \
    cache[(x >> 24) & mask]

def weight(x): #7
    total = 0
    for i in range(32):
        if x & (1 << i):
            total += 1
    return total

def closest_same_weight(x): #8
    for i in range(63):
        if ((x >> i) & 1) != ((x >> (i+1)) & 1):
            return x ^ (3 << i)
    return None
