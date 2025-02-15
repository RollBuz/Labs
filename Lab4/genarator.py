#task 1
def square_generator(N):
    for i in range(1, N + 1):
        yield i ** 2

N = int(input("Enter a number: "))
for square in square_generator(N):
    print(square)

print("------------------------------")

#task 2

def even_num(x):
    for i in range(1,x+1):
        if i%2 ==0:
            yield i

X = int(input("Num: "))
print(",".join(str(i) for i in even_num(X)))

#task 3

def common_multiply(y):
    for i in range(1, y+1):
        if i%3==0 and i%4==0:
            yield i

y = int(input("3 and 4 lcm:"))
for i in common_multiply(y):
    print(y)

#task 4
def squares(a,b):
    for i in range(a, b+1):
        yield i**2

a = int(input("First: "))
b = int(input("Second: "))
for i in squares(a,b):
    print(i)

#task 5
def allnums(n):
    for i in range(n, 0, -1):
        yield i

n = int(input("Num: "))
for i in allnums(n):
    print(i)