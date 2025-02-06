def permutation(string, step=0):
    if len(string) == step:
        print("".join(string))
        return
    
    for i in range(step, len(string)):
        copy = list(string)
        copy[step], copy[i] = copy[i], copy[step]
        permutation(copy, step+1)

a = input("Insert text:")
permutation(a)