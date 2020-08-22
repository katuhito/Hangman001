def padlindrome(word):
    word = word.lower()
    return word[::-1] == word

print(padlindrome("Mother"))
print(padlindrome("Mom"))
