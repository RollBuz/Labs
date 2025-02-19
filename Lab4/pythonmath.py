from math import *

def to_radian(n):
    return n * pi/180

def trapezoid_area(a,b,n):
    return 1/2 * (a+b)*n

def reg_polygone(N, l):
    apothem = l/(2*(tan(pi/N)))
    return (N*l*apothem)/2

def paralelogram(n, h):
    return n*h

x = int(input("Input degree:"))
print(f"Output in radian: {to_radian(x):.6f}")

h = int(input("Height :"))
a = int(input("Base 1 :"))
b = int(input("Base 2 :"))
print(f"Output: {trapezoid_area(a,b,h):.2f}")

length = int(input("Lenght of one side of polygone:"))
num = int(input("Number of sides: "))
print(f"The area is {reg_polygone(num, length):.2f}")

heigth = int(input("Height :"))
base = int(input("Base: "))
print(f"Area of paralelogramm is: {paralelogram(base, heigth)}")