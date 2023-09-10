def eratosthenes(n):
    primes = []
    is_prime = [True] * (n+1)
    for p in range(2, n+1):
        if is_prime[p]:
            primes.append(p)
            for i in range(p*p, n+1, p):
                is_prime[i] = False
    return primes


def print_primes(n):
    primes = eratosthenes(n)
    for p in primes:
        print(p, end=' ')


if __name__ == '__main__':
    n = int(input("Введите верхнюю границу поиска простых чисел: "))
    print(f"Простые числа до {n}:")
    print_primes(n)
