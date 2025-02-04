def is_prime(n):
    if n < 2:
        return False
    return all(n % i != 0 for i in range(2, int(n ** 0.5) + 1))

numbers = [2, 3, 5, 6, 11, 12, 13, 14, 23, 21, 16, 63, 79]

prime_num = list(filter(lambda x: is_prime(x), numbers))

print(f"Prime numbers{prime_num}")

"""
we can write a function without function is_prime()if we do like this:
     prime_numbers = list(filter(lambda n: all(n % i != 0 for i in range(2, int(n ** 0.5) + 1)), numbers))
but its hard to read but its code is compact
"""