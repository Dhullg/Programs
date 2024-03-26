def primes(a):
    primes = []
    for i in range(2, a):
        isPrime = True
        for y in range(2, int(i** 0.5) + 1):
            if i % y == 0:
                isPrime = False
                break
        if isPrime:
            primes.append(i)
    print(primes)
primes(80)
