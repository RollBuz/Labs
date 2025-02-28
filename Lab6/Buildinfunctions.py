import time 
#1
list1 = [1,2,3,4,5]
a = 1
for i in range(len(list1)):
    a *= list1[i]
print(a)
#2
text = "soMe texT For exaMles"
b = 0
c = 0
for i in text:
    if i.islower():
        b +=1
    elif i.isupper():
        c +=1
print(f"The number of lowercase lettes: {b}")
print(f"The number of uppercase lettes: {c}")
#3
pallindrome = "lollol"
pallindrome = list(pallindrome)
if pallindrome == pallindrome[::-1]:
    print("Yes pallindrome")
else:
    print("no not pallindrome")


#4
num = 25100
zaderzhka = 2123

time.sleep(zaderzhka / 1000)

sqrt_value = num ** 0.5  

print(sqrt_value)

#5
tuple1 = (True, True, True)
tuple2 = (1,0,1)
print(all(tuple1))
print(all(tuple2))