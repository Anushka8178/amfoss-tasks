def prime(num):
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True

def primes_up_to_n(n):
    for i in range(2, n + 1):
        if prime(i):
            print(i)

n = int(input("Enter a number: "))
primes_up_to_n(n)
