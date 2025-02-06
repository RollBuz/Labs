def reverse(string):
    string = string.split(" ")
    reversed_string = " ".join(string[::-1])
    return reversed_string

        
s = input("Val:")
print(reverse(s))