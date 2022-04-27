import random


def jacobi(a, n):
    if n <= 0:
        raise Exception("n must be positive")
    if n % 2 == 0:
        raise Exception("n must be odd")
    a = a % n
    result = 1
    while a != 0:
        while a % 2 == 0:
            a = a / 2
            n_mod_8 = n % 8
            if n_mod_8 in (3, 5):
                result = -result
        a, n = n, a
        if a % 4 == 3 and n % 4 == 3:
            result = -result
        a = a % n
    if n == 1:
        return result
    else:
        return 0


def test_primality(n: int, t: int):
    if n < 3 or t < 1:
        raise Exception("Invalid parameters!")
    if n % 2 == 0:
        return "Composite"
    for i in range(1, t):
        a = random.randint(2, n - 2)
        r = pow(a, (n - 1) // 2, n)
        if r != 1 and r != n - 1:
            return "Composite"
        jacobi_symbol = jacobi(a, n)
        if r % n != jacobi_symbol % n:
            return "Composite"
        return "Prime"


print("Jacobi symbols for random numbers")
# http://math.fau.edu/richman/jacobi.htm

for _ in range(10):
    n = random.randint(3, 1000)
    while n % 2 == 0:
        n = random.randint(3, 1000)
    a = random.randint(2, 1000)
    print(f"({a}/{n}) = {jacobi(a, n)}")

print()

print("Solovay Strassen Test")
for _ in range(10):
    random_integer = random.randint(3, 100)
    print(f"Number {random_integer} is {test_primality(random_integer, 100)}")
