def unique_list(list):
    uniquelist=[]
    for i in list:
        if i not in uniquelist:
            uniquelist.append(i)
    return uniquelist

print(unique_list([1,1,1,2,3,3,4,4,5]))