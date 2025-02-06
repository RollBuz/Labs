def spy_game(nums):
    a = []
    for i in nums:
        if i == 0 and (not a or a[-1]==0):
            a.append(i)
        elif i == 7 and len(a) >= 2:
            a.append(i)
            return True
    return False


print(spy_game([1,2,4,0,0,7,5]))
print(spy_game([1,0,2,4,0,5,7]))
print(spy_game([1,7,2,0,4,5,0]))