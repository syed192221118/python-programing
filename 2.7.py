def remove_vowels(s):
    vowels = 'aeiouAEIOU'
    return ''.join([c for c in s if c not in vowels])

s = input("Enter a string: ")
result = remove_vowels(s)
print(f"The string without vowels is: {result}")
