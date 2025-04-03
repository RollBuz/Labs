def square_odd(n):
    for i in range(1, n, 2):
        yield i**2

for square in square_odd(20):   
    print(square)