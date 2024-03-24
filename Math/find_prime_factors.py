from math import sqrt, ceil
# Try to utilize logic from ugly_number


def is_prime(n):
    r = int(sqrt(n)) + 1

    for i in range(2, r):
        if n % i == 0:
            return False
    return True


def get_prime_factors(n):
    r = n // 2 + 1
    prime_factors = []
    for i in range(2, r):
        if is_prime(i) and n % i == 0:
            prime_factors.append(i)
            while n % i == 0:
                n //= i
    return prime_factors if prime_factors else [n]  # For the prime number itself


if __name__ == "__main__":
    print(get_prime_factors(7))