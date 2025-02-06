def palindrome(word):
    word = list(word)
    if word == word[::-1]:
        return True
    return False

print(palindrome("Rollan"))
print(palindrome("madam"))
