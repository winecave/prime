import time
from sys import argv

def is_prime_num(num):
    t0 = time.time()
    count = 0
    try:
        for i in range(3, num -1, 2):
            count += 1
            if num % i == 0:
                return False
        return True
    except Exception as e:
        return False
    finally:
        t1 = time.time()
        print('is_prime_num() elapsed: {0}'.format(t1 - t0))
        print('calcurate count: {0}'.format(count))

def list_n_multiples_of(n, max, list):
    t0 = time.time()
    zero = 0
    dup = 0
    try:
        for num in range(n - 1, max, n):
            #print('index: {0}, num: {1}'.format(num, list[num]))
            if list[num]:
                zero += 1
                list[num] = 0
            else:
                dup += 1
    except Exception as e:
        print('----- index bound exception : num = {0} ----'.format(num))
    finally:
        t1 = time.time()
        print('---- reset: {0}, dup: {1}, dup ratio: {2}% ----'.format(zero, dup, dup*100/(zero+dup)))
        print('list_n_multiples_of {0} elapsed: {1}'.format(n, t1 - t0))

primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, \
          101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193,  \
          197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307]

if len(argv) == 1:
    max = 101
else:
    print(argv[1])
    max = int(argv[1]) + 1

t0 = time.time()
num = [x for x in range(1, max)]

for p in primes:
    print('{0}の倍数-----------------------------------------------------'.format(p))
    list_n_multiples_of(p, max, num)

counter = 0
for i in num:
  if i != 0:
    #print(i)
    counter += 1
print('---- {0} ----'.format(counter))
t1 = time.time()
print('elapsed: {0}'.format(t1 - t0))

print('p: {0}, {1}'.format(p, is_prime_num(524287)))
