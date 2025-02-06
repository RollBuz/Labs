def is_prime(n):
    if n < 2:
        return False
    return all(n % i != 0 for i in range(2, int(n ** 0.5) + 1))

def filter_prime(numbers):
    return list(filter(is_prime, numbers))

numbers = list(map(int, input("Nums:").split()))
prime_numbers = filter_prime(numbers)
print("Prime nums:", prime_numbers)