def is_prime(n):
    d = 2
    while n % d != 0:
        d += 1
    return d == n

print(is_prime(int(input('input number:\n'))))


