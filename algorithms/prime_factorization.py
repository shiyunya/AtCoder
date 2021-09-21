from collections import defaultdict

def prime_factorization(n):
    ret = defaultdict(int)
    i = 2
    while i ** 2 <= n:
        while n % i == 0:
            ret[i] += 1
            n //= i
        i += 1
    if n != 1:
        ret[n] += 1
    return ret


def factors(n):# 0からnまでの数の約数
    factors = [[1] for i in range(n + 1)]
    factors[0] = []
    for i in range(2,len(factors)):
        factors[i].append(i)
        if len(factors[i]) != 2:
            continue
        for j in range(i * 2, len(factors), i):
            factors[j].append(i)
    return factors


n = int(input())
print(prime_factorization(n))
print(factors(n))