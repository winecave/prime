from sys  import argv
from math import sqrt
from time import time

if len(argv) == 1:
    max = 100
else:
    max = int(argv[1])

def eratosthenes(x):
    if x < 2: return []

    primes = [2] + [i for i in range(3, x, 2)]
    sqrt_x = sqrt(x)

    index = -1
    loop_count = 0
    for prime in primes:
        loop_count += 1
        index += 1
        if prime > sqrt_x: break
        if index == 0 or prime == 0:
            continue
        for non_prime in range(index + prime, x//2  , prime):
            loop_count += 1
            primes[non_prime] = 0

    return loop_count, [prime for prime in primes if prime != 0]

loop_count, l = eratosthenes(max)
with open('prime.txt', 'w') as fd:
    for n in l:
        fd.write('{0}\n'.format(n))

print('loop_count: {0:,d}'.format(loop_count))
